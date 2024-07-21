# Employee-salary-prediction💸
It's an Application which predicts the salary of a employee based on the data from stackoverflow . It is trained to predict it from the data using Machine Learning. It's App is designed using python with simple and basic gui.

Dataset available at :
[Salary Dataset](https://insights.stackoverflow.com/survey)

### Libraries used:
- [Matplotlib](https://matplotlib.org/)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)


###  App
- [Streamlit](https://streamlit.io/) A faster way to build and share data apps.Streamlit turns data scripts into shareable web apps,No front end or anything else is required just pure Python.


### Steps
1. Clone the repository
    ```bash
    git clone https://github.com/E980Jessi/Employee-Salary-Prediction.git
    ```
2. Navigate to your project directory
    ```bash
    cd Employee-Salary-Prediction
    ```
3. Install dependencies
    ```bash
    pip install -r requirement.txt
    ```
# To run the predictor
* This model is pre-trained. Run app.py file on the terminal to start the prediction.

    ```bash
    streamlit run app.py
    ```
* Open your web browser and go to  `http://localhost:8501/` to access the application.

# If you want to train the model on your own:

1. **Install Anaconda** : Install anaconda. Once installed, jupyter notebook is installed automatically.

2. **Open the Anaconda prompt** : Navigate to the directory where `SalaryPrediction.ipynb` is located using your terminal.
    ```bash
    cd path/to/the/directory
    ```

3. Start Jupyter Notebook : Run the following command to start the Jupyter Notebook server:
    ```bash
    jupyter notebook
    ```