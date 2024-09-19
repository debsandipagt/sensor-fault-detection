
# Project starts

## 1. Install Anaconda and add `C:\Users\debsa\anaconda3\` to the Windows environment path variable.

## 2. Open VS Code in the folder `sensor-fault-detection`.

## 3. In VS Code, go to Settings -> Path -> Python: Conda Path and add `C:\Users\debsa\anaconda3\`.

## 4. In VS Code, go to Settings -> Path -> Python: Default Interpreter Path and add `C:\Users\debsa\anaconda3\python.exe`.

## 5. Open the with CMD terminal and write the command `git init` to initialize Git (Git is a version control system).

## 6. Create an environment with the command `conda create -p myenv python=3.8.16 -y`.

## 7. Activate the environment with `conda activate ./myenv/`.

## 8. Create a file named `requirements.txt`.

## 9. Run `pip install -r requirements.txt` to install all required libraries.

## 10. Create a `README.md` file to document all steps.

## 11. Create a `.gitignore` file (to specify files/folders that you do not want to push to GitHub).

## 12. Create a `src` folder, and within it, create an `__init__.py` file (this folder acts as a package since it contains `__init__.py`).

## 13. Setup and Installation

- Create a `setup.py` file and use the command `python setup.py install` to install the package.
- Check installed packages using `pip list`.

## 14. Machine Learning Model Building

## 14.1 Create `notebooks` Folder

- Create a `notebooks` folder and use this folder for ML model building with datasets and `.ipynb` files.

## 14.2 Exploratory Data Analysis (EDA) and Feature Engineering

- Conduct Exploratory Data Analysis (EDA) to understand the data.
- Perform feature engineering to prepare the data for modeling.

## 14.3 Model Training

- Train the model using the `RandomForestClassifier`.
- Utilize `GridSearchCV` to find the best parameters for the model.

### Best Parameters:
- `bootstrap`: `True`
- `max_depth`: `None`
- `max_features`: `'sqrt'`
- `min_samples_leaf`: `1`
- `min_samples_split`: `2`
- `n_estimators`: `100`

### Best Score:
- `1.0`

## 15. Create `constant` Folder in `src` and Initialize with `__init__.py`

- Set up a `constant` folder within the `src` directory.
- Inside the `constant` folder, create an `__init__.py` file to store project constants.

## 16. Data Upload Process

- **Create an `upload_data_to_db` folder**: This folder will be used to store files related to uploading data.
- **Inside this folder, add an `upload.ipynb` file**: Create a Jupyter Notebook file (`upload.ipynb`) to handle the process of uploading data to a MongoDB server.

## 17. Exception Handling

- **Create an `exception.py` file**: 
  - **Location**: `src/exception.py`
  - **Purpose**: Manage custom exceptions for your project. Define classes to handle specific error cases and improve error reporting.

## 18. Logger File

- **Create a `logger.py` file**:
  - **Location**: `src/logger.py`
  - **Purpose**: Set up logging configurations for your project. Include functions to initialize and configure a logger to capture and record log messages.

## 19. Utilities Folder

- **Create a `utils` folder**: This folder will contain utility files and classes.
- **Inside the `utils` folder, create an `__init__.py` file**: Initialize the `utils` package by creating an empty `__init__.py` file.
- **Create a `main_utils.py` file**:
  - **Location**: `utils/main_utils.py`
  - **Purpose**: Define a utility class with methods for:
    - Reading YAML files.
    - Saving/loading objects using `pickle`.
    - Handling schema configurations.
    - Providing robust error handling with custom exceptions.

## 20. Configuration

- **`config` Folder**: Create a folder for configuration files.
  - **`model.yaml`**: Add the `model.yaml` file with the following content:
    ```This model.yaml file specifies the models and their hyperparameters to be tuned during the model selection process. You can load and parse this YAML file in your code to use these configurations during model training and hyperparameter tuning.
    
## 21. Component Creation

- **`components` Folder**: Structure the project into modular components.
  - **`__init__.py`**: Initialize the folder as a Python package for streamlined imports.
  - **`data_ingestion.py`**: Manage data loading and preprocessing tasks.
  - **`data_transformation.py`**: Oversee feature engineering and data transformation.
  - **`model_trainer.py`**: Include the logic for training the model.

## 22. Training Pipeline

- Create a `pipeline` folder within the `src` directory.
- In the `pipeline` folder, add a `train_pipeline.py` & `predict_pipeline.py` file.
- Implement the training and prediction pipeline code in `train_pipeline.py` & `predict_pipeline.py`.

## 23. Create `static\css\style.css` for HTML Page Styling

## 24. Create `home.html` file in templates folder to display welcome messare

- Inside the `static` folder, create a `css` subfolder.
- In the `css` subfolder, create a `style.css` file.
- Add the required CSS styles to the `style.css` file for the HTML page design.

## 25. Create `templates\upload_file.htm` for File Upload

- Inside the `templates` folder, create an `upload_file.htm` file.
- Implement the HTML structure for file upload functionality in `upload_file.htm`.
- Ensure the form in the HTML file supports file submission (e.g., using `<form>` with `enctype="multipart/form-data"`).
- Add necessary input fields and buttons for file selection and upload.

## 26. Create `end.html` file in templates folder to display end message

# Deployment in GCP

## 27. Create a New Project in GCP Console

- **Google Cloud Console**: Sign in to your [Google Cloud Console](https://console.cloud.google.com/).
- **Navigate to Manage Resources**: Click on **Manage Resources** from the navigation menu.
- **Create a New Project**:
  - Click **Create New Project**.
  - `sensor-fault-detection`.
  - Click **Create**.

  **Documentation**: [Creating and Managing Projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

## 28. Import Project Code

- **Open Cloud Shell**:
  - Click the **Activate Cloud Shell** button at the top of the console window.
- **Clone the GitHub Repository**:
  - Execute the following command in Cloud Shell:
    ```bash
    git clone https://github.com/debsandipagt/sensoe-fault-detection.git
    ```

  **Documentation**: [Google Cloud Shell](https://cloud.google.com/shell/docs)

## 29. Set Project ID Environment Variable

- **Set the `PROJECT_ID` Variable**:
  - Execute the following command to set the environment variable:
    ```bash
    export PROJECT_ID=<project_id>
    ```

  **Documentation**: [Using Environment Variables in Cloud Shell](https://cloud.google.com/shell/docs/using-environment-variables)

## 30. Build the Docker Image

- **Build the Docker Image**:
  - Navigate to the project directory and build the Docker image with the following command:
    ```bash
    docker build -t gcr.io/${PROJECT_ID}/sensor-fault-detection:v1 .
    ```
- **Check Available Images**:
  - Verify the image is built by running:
    ```bash
    docker images
    ```

  **Documentation**: [Docker Build Command](https://docs.docker.com/engine/reference/commandline/build/)

## 31. Upload the Container Image

- **Authenticate to Container Registry**:
  - Run the following command to configure Docker authentication:
    ```bash
    gcloud auth configure-docker
    ```
- **Upload the Docker Image**:
  - Push the image to Google Container Registry:
    ```bash
    docker push gcr.io/${PROJECT_ID}/sensor-fault-detection:v1
    ```

  **Documentation**: [Docker Push Command](https://docs.docker.com/engine/reference/commandline/push/) and [Authenticating to Google Container Registry](https://cloud.google.com/container-registry/docs/advanced-authentication)

## 32. Create Cluster

- **Set Project ID and Compute Engine Zone**:
  - Configure `gcloud` with your project ID and zone:
    ```bash
    gcloud config set project $PROJECT_ID
    gcloud config set compute/zone us-central1
    ```
- **Create a Kubernetes Cluster**:
  - Create a cluster with 2 nodes:
    ```bash
    gcloud container clusters create sensor-fault-detection-cluster --num-nodes=2
    ```

  **Documentation**: [Creating a Cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster)

## 33. Deploy Application

- **Deploy the Application**:
  - Use `kubectl` to create a deployment:
    ```bash
    kubectl create deployment sensor-fault-detection --image=gcr.io/${PROJECT_ID}/sensor-fault-detection:v1
    ```

  **Documentation**: [Deploying Applications](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

## 34. Expose Your Application to the Internet

- **Expose the Deployment**:
  - Create a service to expose the application:
    ```bash
    kubectl expose deployment sensor-fault-detection --type=LoadBalancer --port 80 --target-port 8080
    ```

  **Documentation**: [Exposing Your Application](https://kubernetes.io/docs/concepts/services-networking/service/)

## 35. Check Service

- **Check the Status of the Service**:
  - Get the external IP address of your service:
    ```bash
    kubectl get service
    ```

  **Documentation**: [Getting Service Details](https://kubernetes.io/docs/concepts/services-networking/service/#retrieving-the-service-details)

## 36. See the App in Action

- **Access the Application**:
  - Open your browser and navigate to the external IP address obtained in the previous step (e.g., `http://<externalIP>:80`).

  **Documentation**: [Accessing Applications](https://cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer)



#################################################################################################################################

### This is end Thanks ###




