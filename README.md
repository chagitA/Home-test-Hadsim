# Home-test-Hadsim
The project contains 2 subprojects:
1. Twitter towers
2. Corona management system

## Twitter towers:
Investigation of different structures and types of towers.
The project allows research on rectangular and triangular towers.
For rectangular towers the user will be able to check the area of the tower or its perimeter, and for triangular towers the user will be able to check the perimeter of the triangle or get a printout of it, in case the data allows it.

## Corona Management System

### Project Description

The Corona Management System is designed to facilitate the management of COVID-19 and vaccination data for a Health Maintenance Organization (HMO). This project involves implementing a partial server-side application and a database for managing records within the HMO's database management system. The system is specifically focused on handling data related to the COVID-19 pandemic, including member information, patient records, and crucial details about the coronavirus epidemic within the context of health fund members.

### Features

- **Member Checkout Display**: The system displays information about health fund members at checkouts.
- **Patient Record Management**: It manages the entry and storage of patient records in the database.
- **COVID-19 Data Handling**: The system stores key details regarding the coronavirus epidemic as it pertains to health fund members.
- **Future Withdrawals**: Data stored can be accessed in the future for various withdrawals, aiding in resource management within the health fund.

### Technologies Used

- React: JavaScript library for building user interfaces.
- Python: Programming language used for server-side development.
- Flask: Web framework for building server-side applications in Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.

### Installation Instructions

To set up the Corona Management System locally, follow these steps:

1. Clone the repository to your local machine.
2. Install Python if not already installed.
3. Install required Python packages using `pip install -r requirements.txt`.
4. Install Node.js if not already installed.
5. Navigate to the `frontend` directory and run `npm install` to install frontend dependencies.
6. Start the backend server by running `python app.py`.
7. Start the frontend server by running `npm start` in the `frontend` directory.
8. Access the application in your web browser at `http://localhost:3000`.


### How to Use
On the home screen of the application, the dummy website appears for entering a new patient and for receiving details for a patient. The client side is partial and not complete, and its purpose is to show how the built server and database will be used in the future.

#### Client-Side Screenshots
![צילום מסך 2024-03-28 170708.png](screeshot%2F%F6%E9%EC%E5%ED%20%EE%F1%EA%202024-03-28%20170708.png)

![צילום מסך 2024-03-28 170716.png](screeshot%2F%F6%E9%EC%E5%ED%20%EE%F1%EA%202024-03-28%20170716.png)

![צילום מסך 2024-03-28 170724.png](screeshot%2F%F6%E9%EC%E5%ED%20%EE%F1%EA%202024-03-28%20170724.png)


### Folder Structure
corona-management-system/ <br> 
│ <br>
├── backend/ # Backend server files <br>
│ ├── queries/ <br>
│ │ ├── patient.py <br>
│ │ ├── summary_view.py <br>
│ │ └── vaccination.py <br>
│ ├── app.py <br>
│ ├── connect_to_sqlserver.py <br>
│ ├── models.py <br>
│ └── validation.py <br>
│ <br>
└── frontend/ # Frontend files <br>
├── src/ # React source files <br>
└── ... <br>

### Assumptions

The following assumptions facilitate the execution of the project:
- There is an assumption that the address entered by the patient is correct and exists (city of residence, street, number).
