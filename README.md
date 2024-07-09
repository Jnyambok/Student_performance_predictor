
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Student performance predictor deployed through Microsoft Azure

![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/93473c75-0a8d-45cd-99d0-2287016199fc)

This project seeks to predict the math scores of students by assessing various dependent factors and has been deployed through:

* Microsoft Azure Cloud Platform
* Running Locally through Flask

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With
[![My Skills](https://skillicons.dev/icons?i=flask,html,python,css,azure,githubactions)](https://skillicons.dev)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## 1. Local Deployment
Clone this repo and open the project via your preferred IDE.
* Clone this repo :
  ```sh
  https://github.com/Jnyambok/end_to_end_azure_ml_project.git
  ```
* Install Flask through pip:
  ```sh
  pip install flask
  ```
 * Then navigate to the "app.py" file in the directory and run:
  ```sh
  python app.py
  ```
  * Open your preferred browser and run paste :
  ```sh
  http://127.0.0.1:5000/predictdata
  ```

## 2. Deployment through Microsoft Azure Cloud Platform
* Fork this repo and proceed to https://azure.microsoft.com/en-in/free/ to sign up for a free Microsoft Azure account
  
* Navigate to the rescource page and search for "Web App". This should take you to the navigation page. Your free subscription will be pre-filled. Select "create new" at the resource group level and provide your preferred name. Provide a web app name that will appear on the search bar name.
  
  ![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/331f34e6-47b5-4b60-a560-da0b05b32462)

* Select **python 3.8** as the runtime stack and select the region **closest to your physical location**
  
 ![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/0e62d117-5fb3-40cf-bed7-6419ba34d10c)

* Navigate to the **Deployment** section and select **enable**. You will be prompted to link your github account and the repo that you forked. A workflow configurations file will be added to your repo which will be used to initiate your CI/CD pipeline. To the bottom, ensure basic authentication is off 
  
 ![image](https://github.com/Jnyambok/end_to_end_azure_ml_project/assets/49593319/473a782e-0588-4857-af4f-3f5fe78ef957)


  

<!-- ROADMAP -->
## Future Works and considerations

- [ ] "Beautify" the home page
- [ ]  Deploy through AWS 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

