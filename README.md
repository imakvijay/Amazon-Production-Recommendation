# Product Recommendation Engine - Amazon	
Hosted webpage: [Recommendation Website](https://amazon-recommendation.azurewebsites.net/)<br>

**Languages Used:** Python, Unix Shell Script, SQL, HTML, CSS, JavaScript<br>
**Frameworks Used:** Scrapy, Open-CV, Sklearn, Numpy, Pandas, Flask<br>
**Database Used:** Sqlite3<br>

Product Recommendation Engine was built to recommend similar products based on the input. Currently, it is developed in a way to accept images from user, and recommend similar products. With small tweaking, the application can be redesigned to recommend similar products on every product pages by passing images internally.

### System architecture
<img src="https://github.com/rampk/amazon-product-recommendation/blob/master/Git-images/System-Architecture.JPG" width="846" height="500"><br><br>

Application will be running on a Flask app, which will call a python script when an image is uploaded. The Python script will then invoke the model, and recommend similar products. Whole application is running in Azure app services, and exposed to internet through a [website](https://amazon-recommendation.azurewebsites.net/)

### Model Architecture
<img src="https://github.com/rampk/amazon-product-recommendation/blob/master/Git-images/Model-Architecture.JPG" width="846" height="500"><br><br>

Three models were stacked on top of each other using Sklearn's Pipeline feature. When an image is uploaded, first model predicts its category, and second model finds the similar products in the category. Third model will be used to find the other similar products based on cosine similarity. 

### Continous Deployment Pipeline
<img src="https://github.com/rampk/amazon-product-recommendation/blob/master/Git-images/CD-Pipeline.JPG" width="846" height="500"><br><br>

When new change is pushed to the [master](https://github.com/rampk/amazon-product-recommendation) branch, application will be build and deployed to [Azure app services](https://amazon-recommendation.azurewebsites.net/) using [Github's workflow](https://github.com/rampk/amazon-product-recommendation/tree/master/.github/workflows)

### Running the application
<img src="https://github.com/rampk/amazon-product-recommendation/blob/master/Git-images/User-Input.JPG" width="846" height="500"><br><br>

User can upload the image using our image upload button feature. When the submit button is clicked, recommendation will be made and user will be redirected to a new page with product recommendations <br><br>

<img src="https://github.com/rampk/amazon-product-recommendation/blob/master/Git-images/Output-Page.JPG" width="846" height="500"><br><br>
