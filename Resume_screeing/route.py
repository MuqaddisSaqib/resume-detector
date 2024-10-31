from flask import render_template, request
from Resume_screeing import app
from Resume_screeing.model_loader import load_model
from Resume_screeing.pdf import pdf_to_text
from Resume_screeing.model_cleaning import cleanResume

# Load the models
tfidf, clf = load_model()


def predict_category(resume_text):
    try:
        resume_text = cleanResume(resume_text)
        resume_tfidf = tfidf.transform([resume_text])
        predicted_category = clf.predict(resume_tfidf)[0]

        category_mapping = {
            0: 'Backend Developer',
            1: 'Cloud Engineer',
            2: 'Data Scientist',
            3: 'Frontend Developer',
            4: 'Full Stack Developer',
            5: 'Machine Learning Engineer',
            6: 'Mobile App Developer (iOS/Android)',
            7: 'Python Developer'
        }

        category_name = category_mapping.get(predicted_category, "unknown")  # Use predicted_category here
        print("Predicted category:", category_name)  # Print the category name
        return category_name  # Return the category name instead of the index
    except Exception as e:
        print("Error during prediction:", str(e))  # Debug statement
        return "Error during prediction"


@app.route('/')
def index():
    return render_template('index.html')





@app.route('/pred', methods=['GET', 'POST'])
def pred():
    if request.method == 'POST':
        if 'resume' in request.files:
            file = request.files['resume']
            filename = file.filename

            if filename.endswith('.pdf'):
                text = pdf_to_text(file)
            elif filename.endswith('.txt'):
                text = file.read().decode('utf-8')
            else:
                return render_template('index.html',
                                       message="Unsupported file type. Please upload a .pdf or .txt file.")

            # Call the prediction function
            predicted_category = predict_category(text)
            print("Predicted category:", predicted_category)  # Debug statement

            # Ensure the predicted_category is not None or empty
            if not predicted_category:
                predicted_category = "No category predicted."

            return render_template('index.html', predicted_category=predicted_category)

    return render_template('index.html')

