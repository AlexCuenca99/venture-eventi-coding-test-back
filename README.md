<a name="readme-top"></a>

<!-- PROJECT LOGO -->
### VentureEventi Coding Interview

![Project Actions](https://github.com/AlexCuenca99/venture-eventi-coding-test-back/actions/workflows/testing.yml/badge.svg)
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
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/AlexCuenca99/venture-eventi-coding-test-back/)

Solution to the web problem proposed in the VentureEventi technical interview for the position of Back-end developer.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![React][React.js]][React-url]
* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

The needs are:

* python

  ```sh
  python --version
  ```

### Installation

1. Create a new Python virtual environment
2. Clone the repo

   ```sh
   git clone https://github.com/AlexCuenca99/venture-eventi-coding-test-back/tree/main
   ```

3. Install requirements

   ```sh
   pip install -r requirements.txt
   ```

4. Create .env file and add .env.dist variables

5. Run server

   ```sh
   python manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Charts and Reports

![Charts and Reports][charts-screenshot]

Dashboard page shows a resume of the entire app activities and proccesses. On "Cantidad de transacciones por intevalo" you can filter the transactions. Meanwhile, on "Cantidad de transacciones por tipo de movimiento" you can see all transactions grouped by their transaction type.

### Movement Types

![Movement Types][movement-types-screenshot]

Movement types page shows all created movement types on the app. You can perform CRUD (Create, Retrieve, Update, Delete) operations.

### Bank movements

![Bank movements][bank-movements-screenshot]

Bank movements page shows a header who lets you choose between app clients. When you select a client the bottom table will be render with all transactions of the selected client.

You can update and create a new client when you do not select any user. Also you can update the client date when one is selected.

Finally, you can create new transactions to the selected client. It will be let choose you the movement types and the value.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Alex Cuenca - [@alex_pcr99](https://twitter.com/alex_pcr99) - <alex-patricio1999@hotmail.com>

Project Link: [https://github.com/AlexCuenca99/venture-eventi-coding-test-back](https://github.com/AlexCuenca99/venture-eventi-coding-test-back)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Img Shields](https://shields.io)
* [React Icons](https://react-icons.github.io/react-icons/search)
* [Lodash](https://lodash.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Semantic UI React](https://react.semantic-ui.com/)
* [django-filter](https://django-filter.readthedocs.io/en/stable/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: assets/images/dashboard.png
[charts-screenshot]: assets/images/charts.png
[movement-types-screenshot]: assets/images/movement-types.png
[bank-movements-screenshot]: assets/images/bank-movements.png
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
