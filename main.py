from tensorflow.keras.models import load_model

print("TensorFlow version:", __import__("tensorflow").__version__)
print("Keras version:", __import__("keras").__version__)
model = load_model(".\model\TSR (model_by_gayatri).h5")  # Replace with your model's file path
print("Model loaded successfully!")
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serves the HTML file

if __name__ == '__main__':
    app.run(debug=True)
