![](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/12/spark21-2048x1365.png)

# Streamlit for Model Deployment
One of the most critical issues with regard to model creation was that the model itself would remain stuck in the notebook or .py file on Spyder.  The ability to share a model with people who cannot use either of these platforms has been rather limited till I discovered Streamlit.  Streamlit is a library in Python allowing for seamless model creation and deployment.

Through the use of very few lines of code an interactive html interface is opened on the web-browser which can be used by anyone to get an understanding of the model and suggest course corrections.  It allows for those cryptic lines of code to suddenly see the light of day in a manner that allows the viewer to be just as participative in the model creation process as the creator himself.

I have created this example which consists of two files.  One notebook file - which is the base model and another .py file which has to be run in conjunction to deploy the Streamlit file on a web-browser.

Key code snippets used in this file:
-  
- Pickle for storing a model
- Set option to display of max columns
-  Application of Label Encoder for coding Categorical values
- EDA with heatmaps using .corr, pairplots
- Application of Randomised Search CV with parameter distribution
- The key parameters for streamlit is in the .py file

To run the .py file please navigate to the file through the Anaconda Command prompt and type the following code:

## streamlit run app2.py


You can view the python code for the model by clicking [here](https://github.com/ArijitChakrabarti/Cars-Streamlit---Arijit/blob/main/Learning%20Streamlit.ipynb) & [here](https://github.com/ArijitChakrabarti/Cars-Streamlit---Arijit/blob/main/app2.py) to see the .py file for Streamlit deployment.
