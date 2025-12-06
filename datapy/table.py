import os
import mysql.connector
import hashlib
from dotenv import load_dotenv
from mysql.connector import connection, errorcode

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv('db_host'),
    user=os.getenv('db_user'),
    password=os.getenv('db_pass'),
    database="bankmodel"
)


def hashed(value):
    if value:
        return hashlib.sha256(value.encode()).hexdigest()[:32]


print("Host: ", hashed("db_host"))
print("User: ", hashed("db_user"))

mycursor = mydb.cursor()

mycursor.execute("use bankmodel")

mycursor.execute("DROP TABLE IF EXISTS ATMTransaction")
mycursor.execute("DROP TABLE IF EXISTS CityATM")
mycursor.execute("DROP TABLE IF EXISTS TransactionForATM")
mycursor.execute("DROP TABLE IF EXISTS ATM")
mycursor.execute("DROP TABLE IF EXISTS Brand")
mycursor.execute("DROP TABLE IF EXISTS ATMStatus")
mycursor.execute("DROP TABLE IF EXISTS BankAccPromotion")
mycursor.execute("DROP TABLE IF EXISTS Promotion")
mycursor.execute("DROP TABLE IF EXISTS BranchDepartment")
mycursor.execute("DROP TABLE IF EXISTS Employee")
mycursor.execute("DROP TABLE IF EXISTS CountryOfEmployment")
mycursor.execute("DROP TABLE IF EXISTS Position")
mycursor.execute("DROP TABLE IF EXISTS Loan")
mycursor.execute("DROP TABLE IF EXISTS LoanType")
mycursor.execute("DROP TABLE IF EXISTS LoanStatus")
mycursor.execute("DROP TABLE IF EXISTS Transaction")
mycursor.execute("DROP TABLE IF EXISTS TransactionType")
mycursor.execute("DROP TABLE IF EXISTS TransactionStatus")
mycursor.execute("DROP TABLE IF EXISTS BankAccount")
mycursor.execute("DROP TABLE IF EXISTS AccountType")
mycursor.execute("DROP TABLE IF EXISTS Currency")
mycursor.execute("DROP TABLE IF EXISTS AccountStatus")
mycursor.execute("DROP TABLE IF EXISTS Language")
mycursor.execute("DROP TABLE IF EXISTS Identification")
mycursor.execute("DROP TABLE IF EXISTS Customer")
mycursor.execute("DROP TABLE IF EXISTS MainNationality")
mycursor.execute("DROP TABLE IF EXISTS Citizenship")
mycursor.execute("DROP TABLE IF EXISTS Gender")
mycursor.execute("DROP TABLE IF EXISTS ClientStatus")
mycursor.execute("DROP TABLE IF EXISTS Branch")
mycursor.execute("DROP TABLE IF EXISTS City")
mycursor.execute("DROP TABLE IF EXISTS Department")
mycursor.execute("DROP TABLE IF EXISTS Region")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Gender("
    "genderId INT PRIMARY KEY, "
    "name VARCHAR(10) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS ClientStatus("
    "clientStatusId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS MainNationality("
    "nationalityId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Citizenship("
    "citizenshipId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Language("
    "languageId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS AccountType("
    "typeId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Currency("
    "currencyId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS AccountStatus("
    "statusId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS TransactionType("
    "transactionTypeId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS TransactionStatus("
    "statusId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS LoanType("
    "typeId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS LoanStatus("
    "statusId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE, "
    "description VARCHAR(100))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Promotion("
    "promotionId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Region("
    "regionId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS ATMStatus("
    "statusId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Brand("
    "brandId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS TransactionForATM("
    "transactionId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS CountryOfEmployment("
    "countryOfEmploymentId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS `Position`("
    "positionId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL UNIQUE)"
)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Department("
    "departmentId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL, "
    "phone VARCHAR(15) NOT NULL, "
    "dateCreated DATE NOT NULL, "
    "email VARCHAR(50) NOT NULL UNIQUE, "
    "regionId INT NOT NULL, "
    "constraint FK_Department_Region FOREIGN KEY(regionId) REFERENCES Region(regionId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS City("
    "cityId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL, "
    "regionId INT NOT NULL, "
    "constraint FK_City_Region FOREIGN KEY(regionId) REFERENCES Region(regionId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Branch("
    "branchId INT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL, "
    "address VARCHAR(100) NOT NULL, "
    "postalCode VARCHAR(10) NOT NULL, "
    "cityId INT NOT NULL, "
    "dateOpened DATE NOT NULL, "
    "phone VARCHAR(15) NOT NULL, "
    "departmentId INT NOT NULL, "
    "constraint UQ_Branch UNIQUE(name, address, postalCode), "
    "constraint FK_Branch_City FOREIGN KEY(cityId) REFERENCES City(cityId), "
    "constraint FK_Branch_Department FOREIGN KEY(departmentId) REFERENCES Department(departmentId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS BranchDepartment("
    "branchId INT NOT NULL, "
    "departmentId INT NOT NULL, "
    "PRIMARY KEY(branchId, departmentId), "
    "constraint FK_BranchDepartment_Branch FOREIGN KEY(branchId) REFERENCES Branch(branchId), "
    "constraint FK_BranchDepartment_Department FOREIGN KEY(departmentId) REFERENCES Department(departmentId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Customer("
    "customerId INT PRIMARY KEY, "
    "firstName VARCHAR(50) NOT NULL, "
    "lastName VARCHAR(50) NOT NULL, "
    "dateOfBirth DATE NOT NULL, "
    "street VARCHAR(100) NOT NULL, "
    "postalCode VARCHAR(10) NOT NULL, "
    "phone VARCHAR(15) NOT NULL, "
    "email VARCHAR(50) NOT NULL UNIQUE, "
    "dateJoined DATE NOT NULL, "
    "nationalityId INT NOT NULL, "
    "citizenshipId INT NOT NULL, "
    "genderId INT NOT NULL, "
    "clientStatusId INT NOT NULL, "
    "constraint FK_Customer_MainNationality FOREIGN KEY(nationalityId) REFERENCES MainNationality(nationalityId), "
    "constraint FK_Customer_Citizenship FOREIGN KEY(citizenshipId) REFERENCES Citizenship(citizenshipId), "
    "constraint FK_Customer_Gender FOREIGN KEY(genderId) REFERENCES Gender(genderId), "
    "constraint FK_Customer_ClientStatus FOREIGN KEY(clientStatusId) REFERENCES ClientStatus(clientStatusId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Identification("
    "identificationId INT PRIMARY KEY, "
    "customerId INT NOT NULL, "
    "identificationTypeId INT NOT NULL, "
    "identificationNumber VARCHAR(50) NOT NULL UNIQUE, "
    "dateIssued DATE NOT NULL, "
    "dateExpired DATE, "
    "constraint FK_Identification_Customer FOREIGN KEY(customerId) REFERENCES Customer(customerId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS BankAccount("
    "accountId INT PRIMARY KEY, "
    "customerId INT NOT NULL, "
    "balance FLOAT NOT NULL, "
    "creditScore INT NOT NULL, "
    "dateCreated DATE NOT NULL, "
    "typeId INT NOT NULL, "
    "currencyId INT NOT NULL, "
    "languageId INT NOT NULL, "
    "statusId INT NOT NULL, "
    "constraint UQ_BankAccount UNIQUE(customerId, dateCreated), "
    "constraint FK_BankAccount_Customer FOREIGN KEY(customerId) REFERENCES Customer(customerId), "
    "constraint FK_BankAccount_AccountType FOREIGN KEY(typeId) REFERENCES AccountType(typeId), "
    "constraint FK_BankAccount_Currency FOREIGN KEY(currencyId) REFERENCES Currency(currencyId), "
    "constraint FK_BankAccount_Language FOREIGN KEY(languageId) REFERENCES Language(languageId), "
    "constraint FK_BankAccount_AccountStatus FOREIGN KEY(statusId) REFERENCES AccountStatus(statusId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS BankAccPromotion("
    "promotionId INT NOT NULL, "
    "accountId INT NOT NULL, "
    "PRIMARY KEY(promotionId, accountId), "
    "constraint FK_BankAccPromotion_Promotion FOREIGN KEY(promotionId) REFERENCES Promotion(promotionId), "
    "constraint FK_BankAccPromotion_BankAccount FOREIGN KEY(accountId) REFERENCES BankAccount(accountId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Loan("
    "loanId INT PRIMARY KEY, "
    "accountId INT NOT NULL, "
    "typeId INT NOT NULL, "
    "amount FLOAT NOT NULL, "
    "startDate DATE NOT NULL, "
    "finishDate DATE NOT NULL, "
    "statusId INT NOT NULL, "
    "constraint UQ_Loan UNIQUE(accountId, startDate), "
    "constraint FK_Loan_LoanType FOREIGN KEY(typeId) REFERENCES LoanType(typeId), "
    "constraint FK_Loan_LoanStatus FOREIGN KEY(statusId) REFERENCES LoanStatus(statusId), "
    "constraint FK_Loan_BankAccount FOREIGN KEY(accountId) REFERENCES BankAccount(accountId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Transaction("
    "transactionId INT PRIMARY KEY, "
    "accountId INT NOT NULL, "
    "amount FLOAT NOT NULL, "
    "dateTime DATETIME NOT NULL, "
    "description VARCHAR(255), "
    "code VARCHAR(10) NOT NULL, "
    "transactionTypeId INT NOT NULL, "
    "statusId INT NOT NULL, "
    "fee FLOAT, "
    "constraint FK_Transaction_BankAccount FOREIGN KEY(accountId) REFERENCES BankAccount(accountId), "
    "constraint FK_Transaction_TransactionType FOREIGN KEY(transactionTypeId) REFERENCES TransactionType(transactionTypeId), "
    "constraint FK_Transaction_TransactionStatus FOREIGN KEY(statusId) REFERENCES TransactionStatus(statusId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS ATM("
    "atmId INT PRIMARY KEY, "
    "brandId INT NOT NULL, "
    "dateInstalled DATE NOT NULL, "
    "currentCashAmount FLOAT NOT NULL, "
    "cashCapacity FLOAT NOT NULL, "
    "statusId INT NOT NULL, "
    "maintenanceDate DATE, "
    "address VARCHAR(100) NOT NULL, "
    "postalCode VARCHAR(10) NOT NULL, "
    "constraint UQ_ATM UNIQUE(address, postalCode), "
    "constraint FK_ATM_Brand FOREIGN KEY(brandId) REFERENCES Brand(brandId), "
    "constraint FK_ATM_ATMStatus FOREIGN KEY(statusId) REFERENCES ATMStatus(statusId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS ATMTransaction("
    "transactionId INT NOT NULL, "
    "atmId INT NOT NULL, "
    "PRIMARY KEY(transactionId, atmId), "
    "constraint FK_ATMTransaction_TransactionForATM FOREIGN KEY(transactionId) REFERENCES TransactionForATM(transactionId), "
    "constraint FK_ATMTransaction_ATM FOREIGN KEY(atmId) REFERENCES ATM(atmId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS CityATM("
    "cityId INT NOT NULL, "
    "atmId INT NOT NULL, "
    "PRIMARY KEY(cityId, atmId), "
    "constraint FK_CityATM_City FOREIGN KEY(cityId) REFERENCES City(cityId), "
    "constraint FK_CityATM_ATM FOREIGN KEY(atmId) REFERENCES ATM(atmId))"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Employee("
    "employeeId INT PRIMARY KEY, "
    "firstName VARCHAR(50) NOT NULL, "
    "lastName VARCHAR(50) NOT NULL, "
    "positionId INT NOT NULL, "
    "phone VARCHAR(15) NOT NULL, "
    "email VARCHAR(50) NOT NULL UNIQUE, "
    "dateHired DATE NOT NULL, "
    "dateLeft DATE, "
    "salary FLOAT NOT NULL, "
    "nationalityId INT NOT NULL, "
    "countryOfEmploymentId INT NOT NULL, "
    "citizenshipId INT NOT NULL, "
    "branchId INT NOT NULL, "
    "departmentId INT NOT NULL, "
    "constraint FK_Employee_MainNationality FOREIGN KEY(nationalityId) REFERENCES MainNationality(nationalityId), "
    "constraint FK_Employee_Citizenship FOREIGN KEY(citizenshipId) REFERENCES Citizenship(citizenshipId), "
    "constraint FK_Employee_CountryOfEmployment FOREIGN KEY(countryOfEmploymentId) REFERENCES CountryOfEmployment(countryOfEmploymentId), "
    "constraint FK_Employee_Branch FOREIGN KEY(branchId) REFERENCES Branch(branchId), "
    "constraint FK_Employee_Department FOREIGN KEY(departmentId) REFERENCES Department(departmentId), "
    "constraint FK_Employee_Position FOREIGN KEY(positionId) REFERENCES `Position`(positionId))"
)

mydb.commit()

print("Tables created successfully")

mydb.close()
