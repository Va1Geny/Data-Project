import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv('db_host'),
    user=os.getenv('db_user'),
    password=os.getenv('db_pass'),
    database="bankmodel"
)

mycursor = mydb.cursor()

gender_data = [
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Non-binary'),
]

client_status_data = [
    (1, 'Active'),
    (2, 'Inactive'),
    (3, 'Blocked'),
    (4, 'VIP'),
    (5, 'Corporate'),
    (6, 'Pending Verification'),
    (7, 'Closed'),
]

main_nationality_data = [
    (1, 'American'),
    (2, 'Canadian'),
    (3, 'British'),
    (4, 'Irish'),
    (5, 'Italian'),
    (6, 'Australian'),
    (7, 'French'),
]

citizenship_data = [
    (1, 'USA'),
    (2, 'Canada'),
    (3, 'UK'),
    (4, 'Ireland'),
    (5, 'Italy'),
    (6, 'Australia'),
    (7, 'France'),
    (8, 'Ukraine'),
    (9, 'Belgium'),
    (10, 'Germany'),
    (11, 'Austria'),
    (12, 'Argentina'),
    (13, 'Spain'),
    (14, 'Portugal'),
    (15, 'Luxemburg'),
]

language_data = [
    (1, 'English'),
    (2, 'Spanish'),
    (3, 'French'),
    (4, 'German'),
    (5, 'Chinese'),
    (6, 'Russian'),
    (7, 'Japanese'),
    (8, 'Ukrainian'),
    (9, 'Moldovian'),
    (10, 'Urdu'),
    (11, 'Hindi'),
    (12, 'Italian'),
    (13, 'Romanian'),
    (14, 'Armenian'),
    (15, 'Polish'),
]

account_type_data = [
    (1, 'Checking'),
    (2, 'Savings'),
    (3, 'Credit'),
    (4, 'Investment'),
    (5, 'Business'),
]

account_status_data = [
    (1, 'Active'),
    (2, 'Frozen'),
    (3, 'Closed'),
    (4, 'Under Review'),
    (5, 'Dormant'),
]

currency_data = [
    (1, 'USD'),
    (2, 'EUR'),
    (3, 'GBP'),
    (4, 'JPY'),
    (5, 'CHF'),
    (6, 'CAD'),
    (7, 'AUD'),
    (8, 'CNY'),
    (9, 'LEU'),
    (10, 'RON'),
    (11, 'ISK'),
    (12, 'KRW'),
    (13, 'HUF'),
    (14, 'DKK'),
    (15, 'SKK'),
]

transaction_type_data = [
    (1, 'Deposit'),
    (2, 'Withdrawal'),
    (3, 'Transfer'),
    (4, 'Payment'),
    (5, 'Fee'),
    (6, 'Interest'),
]

transaction_status_data = [
    (1, 'Completed'),
    (2, 'Pending'),
    (3, 'Failed'),
    (4, 'Cancelled'),
    (5, 'Refunded'),
]

loan_type_data = [
    (1, 'Mortgage'),
    (2, 'Personal Loan'),
    (3, 'Auto Loan'),
    (4, 'Student Loan'),
]

loan_status_data = [
    (1, 'Active'),
    (2, 'Paid Off'),
    (3, 'Defaulted'),
    (4, 'Refinanced'),
    (5, 'Approved'),
    (6, 'Rejected'),
]

promotion_data = [
    (1, 'New Customer Bonus'),
    (2, 'High Interest Savings'),
    (3, 'Referral Reward'),
    (4, 'Student Special'),
    (5, 'Holiday Cashback'),
]

region_data = [
    (1, 'New York State'),
    (2, 'New Jersey'),
    (3, 'Connecticut'),
    (4, 'California'),
    (5, 'Texas'),
    (6, 'Colorado'),
    (7, 'Florida'),
    (8, 'Arizona'),
    (9, 'New Mexico'),
    (10, 'Washington'),
    (11, 'Illinois'),
    (12, 'Maine'),
    (13, 'Hawaii'),
    (14, 'Alaska'),
    (15, 'Ontario'),
]

atm_status_data = [
    (1, 'Online'),
    (2, 'Offline'),
    (3, 'Out of Cash'),
    (4, 'Maintenance'),
    (5, 'Error'),
]

brand_data = [
    (1, 'NCR'),
    (2, 'Diebold Nixdorf'),
    (3, 'Hyosung'),
    (4, 'GRG Banking'),
]

position_data = [
    (1, 'Branch Manager'),
    (2, 'Senior Teller'),
    (3, 'Teller'),
    (4, 'Loan Officer'),
    (5, 'Financial Advisor'),
    (6, 'Security Guard'),
    (7, 'IT Support'),
    (8, 'CEO'),
    (9, 'CTO'),
    (10, 'CBM'),
    (11, 'Sales'),
    (12, 'Customer Service'),
    (13, 'Sub Contract'),
    (14, 'Cybersecurity'),
    (15, 'SOC Analyst'),
]

country_of_employment_data = [
    (1, 'USA'),
    (2, 'Canada'),
    (3, 'UK'),
    (4, 'Germany'),
]

department_data = [
    (1, 'Operations', '646-555-0101', '2010-01-01', 'ops@bank.com', 1),
    (2, 'Retail Sales', '646-555-0102', '2010-01-01', 'sales@bank.com', 1),
    (3, 'Loan Dept', '646-555-0103', '2011-03-15', 'loans@bank.com', 1),
    (4, 'Wealth Mgmt', '646-555-0104', '2012-06-20', 'wealth@bank.com', 1),
    (5, 'Security', '646-555-0105', '2010-01-01', 'security@bank.com', 1),
    (6, 'IT Support', '646-555-0106', '2010-05-10', 'it@bank.com', 2),
    (7, 'HR', '646-555-0107', '2010-02-01', 'hr@bank.com', 1),
    (8, 'Marketing', '646-555-0108', '2013-09-01', 'marketing@bank.com', 1),
    (9, 'Legal', '646-555-0109', '2011-11-11', 'legal@bank.com', 1),
    (10, 'Compliance', '646-555-0110', '2012-01-20', 'compliance@bank.com', 1),
    (11, 'Customer Service', '646-555-0111', '2010-01-01', 'service@bank.com', 2),
    (12, 'Investment Banking', '646-555-0112', '2015-04-01', 'invest@bank.com', 1),
    (13, 'Risk Management', '646-555-0113', '2014-07-15', 'risk@bank.com', 1),
    (14, 'Audit', '646-555-0114', '2011-08-08', 'audit@bank.com', 1),
    (15, 'Facilities', '646-555-0115', '2010-01-01', 'facilities@bank.com', 2),
]

city_data = [
    (1, 'New York', 1),
    (2, 'Brooklyn', 1),
    (3, 'Queens', 1),
    (4, 'Bronx', 1),
    (5, 'Staten Island', 1),
    (6, 'Jersey City', 2),
    (7, 'Newark', 2),
    (8, 'Hoboken', 2),
    (9, 'Stamford', 3),
    (10, 'Greenwich', 3),
    (11, 'Los Angeles', 4),
    (12, 'San Francisco', 4),
    (13, 'Austin', 5),
    (14, 'Dallas', 5),
    (15, 'Houston', 5),
]

branch_data = [
    (1, 'Downtown HQ', '100 Main St', '10001', 1, '2010-01-15', '+15551001', 1),
    (2, 'North Side', '250 North Ave', '10020', 1, '2011-03-20', '+15551002', 2),
    (3, 'West End', '45 West Blvd', '10030', 1, '2012-05-10', '+15551003', 3),
    (4, 'East Village', '78 East Rd', '10040', 1, '2013-07-05', '+15551004', 4),
    (5, 'Airport Branch', '1 Terminal Way',
     '11000', 1, '2014-02-28', '+15551005', 5),
    (6, 'Mall Kiosk', '500 Shop Ln', '10050', 1, '2015-06-12', '+15551006', 6),
    (7, 'Brooklyn Main', '200 Atlantic Ave',
     '11201', 2, '2016-08-22', '+15551007', 7),
    (8, 'Queens Plaza', '30 Queens Blvd', '11101', 3, '2017-04-18', '+15551008', 8),
    (9, 'Bronx Center', '40 Grand Concourse',
     '10451', 4, '2018-09-30', '+15551009', 9),
    (10, 'Staten Island', '10 Richmond Rd',
     '10301', 5, '2019-01-25', '+15551010', 10),
    (11, 'Jersey City', '50 Hudson St', '07030', 6, '2020-03-11', '+15551011', 11),
    (12, 'Newark Branch', '10 Broad St', '07102', 7, '2021-05-16', '+15551012', 12),
    (13, 'Hoboken', '5 Washington St', '07030', 8, '2022-02-08', '+15551013', 13),
    (14, 'Stamford', '100 Tresser Blvd', '06901', 9, '2023-07-21', '+15551014', 14),
    (15, 'Greenwich', '20 Putman Ave', '06830', 10, '2024-01-10', '+15551015', 15),
]

branch_department_data = [
    (1, 1), (1, 2), (1, 3), (1, 5), (1, 7),
    (2, 2), (2, 3), (2, 5),
    (3, 2), (3, 4),
    (4, 2), (4, 3),
    (5, 2), (5, 11),
    (6, 2),
    (7, 1), (7, 2), (7, 3),
    (8, 2),
    (9, 2), (9, 3),
    (10, 2),
    (11, 2), (11, 6),
    (12, 2), (12, 3),
]

customer_data = [
    (1, 'John', 'Smith', '1985-03-12', 1, '1924 Elm Pl', '10001',
     '+15550101', 'john.smith@email.com', '2020-01-15', 1, 1, 1),
    (2, 'Maria', 'Garcia', '1990-07-22', 2, '509 Chestnut St',
     '10002', '+15550102', 'maria.g@email.com', '2020-02-20', 2, 2, 1),
    (3, 'Robert', 'Johnson', '1978-11-05', 1, '4606 Willow Blvd',
     '10003', '+15550103', 'bobj@email.com', '2019-11-10', 1, 1, 4),
    (4, 'Sarah', 'Williams', '1995-09-30', 2, '4112 Lake Pl', '10004',
     '+15550104', 'sarah.w@email.com', '2021-05-12', 1, 1, 1),
    (5, 'Michael', 'Brown', '1982-04-18', 1, '3757 Spruce Blvd',
     '10005', '+15550105', 'mbrown@email.com', '2018-08-25', 3, 3, 2),
    (6, 'Emily', 'Jones', '1992-12-01', 2, '2386 Birch Cir', '10006',
     '+15550106', 'emily.j@email.com', '2022-01-30', 1, 1, 1),
    (7, 'David', 'Miller', '1975-06-15', 1, '1779 Cedar St', '10007',
     '+15550107', 'd.miller@email.com', '2017-03-14', 1, 1, 4),
    (8, 'Jessica', 'Davis', '1988-08-08', 2, '9035 Hill Rd', '10008',
     '+15550108', 'jess.d@email.com', '2020-09-09', 4, 4, 1),
    (9, 'James', 'Wilson', '1999-02-28', 1, '1524 Lake Way', '10009',
     '+15550109', 'jwilson@email.com', '2023-06-01', 1, 1, 6),
    (10, 'Jennifer', 'Taylor', '1984-10-10', 2, '9774 Maple Ln', '10010',
     '+15550110', 'jen.taylor@email.com', '2019-12-25', 5, 5, 3),
    (11, 'William', 'Anderson', '1969-01-20', 1, '7012 Pine Blvd',
     '10011', '+15550111', 'bill.a@email.com', '2015-07-07', 1, 1, 5),
    (12, 'Elizabeth', 'Thomas', '1991-05-05', 2, '620 Hill Dr',
     '10012', '+15550112', 'beth.t@email.com', '2021-02-14', 1, 1, 1),
    (13, 'Christopher', 'Martinez', '1987-03-15', 1, '588 Oak Ave',
     '10013', '+15550113', 'chris.m@email.com', '2019-04-01', 2, 2, 1),
    (14, 'Lisa', 'Hernandez', '1993-11-22', 2, '1635 Spruce Ave',
     '10014', '+15550114', 'lisa.h@email.com', '2022-10-10', 1, 1, 1),
    (15, 'Daniel', 'Moore', '1980-09-17', 1, '3682 Maple Dr', '10015',
     '+15550115', 'dan.moore@email.com', '2018-01-05', 1, 1, 2),
]

identification_data = [
    (1, 1, 1, 'ID123456', '2020-01-01', '2030-01-01'),
    (2, 1, 1, 'ID123457', '2020-01-01', '2030-01-01'),
    (3, 2, 1, 'ID234567', '2019-06-15', '2029-06-15'),
    (4, 3, 1, 'ID345678', '2018-11-05', '2028-11-05'),
    (5, 4, 1, 'ID456789', '2021-05-12', '2031-05-12'),
    (6, 5, 1, 'ID567890', '2018-08-25', '2028-08-25'),
    (7, 6, 1, 'ID678901', '2022-01-30', '2032-01-30'),
    (8, 7, 1, 'ID789012', '2017-03-14', '2027-03-14'),
    (9, 8, 1, 'ID890123', '2020-09-09', '2030-09-09'),
    (10, 9, 1, 'ID901234', '2023-06-01', '2033-06-01'),
    (11, 10, 1, 'ID012345', '2019-12-25', '2029-12-25'),
    (12, 11, 1, 'ID112233', '2015-07-07', '2025-07-07'),
    (13, 12, 1, 'ID223344', '2021-02-14', '2031-02-14'),
    (14, 13, 1, 'ID334455', '2019-04-01', '2029-04-01'),
    (15, 14, 1, 'ID445566', '2022-10-10', '2032-10-10'),
]

bank_account_data = [
    (101, 1, 1, 5400.5, '2020-01-16', 720, 1, 1, 1),
    (102, 1, 2, 12000.0, '2020-06-01', 720, 1, 1, 1),
    (103, 2, 1, 320.0, '2020-02-21', 650, 1, 2, 1),
    (104, 3, 5, 150000.0, '2019-11-15', 800, 1, 1, 1),
    (105, 4, 1, 1200.75, '2021-05-13', 680, 2, 1, 1),
    (106, 5, 3, -500.0, '2018-08-26', 550, 1, 1, 2),
    (107, 6, 2, 5000.0, '2022-02-01', 710, 1, 1, 1),
    (108, 7, 4, 25000.0, '2017-03-20', 790, 1, 1, 1),
    (109, 8, 1, 890.2, '2020-09-10', 695, 3, 1, 1),
    (110, 9, 1, 100.0, '2023-06-02', 0, 1, 1, 1),
    (111, 10, 3, -1200.0, '2019-12-26', 620, 1, 1, 3),
    (112, 11, 5, 75000.0, '2015-07-08', 760, 1, 1, 1),
    (113, 12, 2, 3300.5, '2021-02-15', 700, 2, 1, 1),
    (114, 13, 1, 4500.0, '2019-04-02', 730, 1, 3, 1),
    (115, 14, 1, 2100.25, '2022-10-11', 715, 1, 2, 1),
]

loan_data = [
    (1, 101, 1, 350000.0, '2020-02-01', '2050-02-01', 1),
    (2, 102, 3, 25000.0, '2021-06-15', '2026-06-15', 1),
    (3, 103, 2, 5000.0, '2022-01-10', '2024-01-10', 1),
    (4, 104, 1, 500000.0, '2019-12-01', '2049-12-01', 1),
    (5, 105, 4, 40000.0, '2018-09-01', '2028-09-01', 1),
    (6, 107, 2, 10000.0, '2023-01-05', '2025-01-05', 1),
    (7, 108, 3, 30000.0, '2020-05-20', '2025-05-20', 2),
    (8, 109, 2, 2000.0, '2023-08-01', '2024-02-01', 1),
    (9, 111, 2, 15000.0, '2019-11-11', '2022-11-11', 3),
    (10, 112, 1, 200000.0, '2016-03-15', '2036-03-15', 1),
    (11, 113, 3, 18000.0, '2021-07-01', '2026-07-01', 1),
    (12, 114, 2, 3000.0, '2022-04-10', '2023-04-10', 2),
    (13, 115, 4, 25000.0, '2020-08-25', '2030-08-25', 1),
    (14, 101, 2, 5000.0, '2021-12-01', '2022-12-01', 2),
    (15, 104, 3, 60000.0, '2023-01-15', '2028-01-15', 1),
]

transaction_data = [
    (1001, 101, -50.0, '2023-10-01 10:00:00', 'Grocery Store', 'TX001', 2, 1, 0.0),
    (1002, 101, 2000.0, '2023-10-01 09:00:00',
     'Salary Deposit', 'TX002', 1, 4, 0.0),
    (1003, 102, 100.0, '2023-10-02 14:30:00',
     'Interest Payment', 'TX003', 1, 3, 0.0),
    (1004, 103, -20.0, '2023-10-03 11:15:00',
     'ATM Withdrawal', 'TX004', 3, 1, 2.5),
    (1005, 104, -5000.0, '2023-10-04 16:00:00',
     'Vendor Payment', 'TX005', 2, 4, 10.0),
    (1006, 105, -15.99, '2023-10-05 19:20:00', 'Netflix Sub', 'TX006', 2, 5, 0.0),
    (1007, 107, 500.0, '2023-10-06 10:00:00', 'Cash Deposit', 'TX007', 1, 3, 0.0),
    (1008, 108, 150.0, '2023-10-07 09:45:00', 'Dividend', 'TX008', 1, 2, 0.0),
    (1009, 109, -45.0, '2023-10-08 20:00:00', 'Restaurant', 'TX009', 2, 4, 0.0),
    (1010, 111, -100.0, '2023-10-09 12:00:00', 'Late Fee', 'TX010', 4, 4, 0.0),
    (1011, 112, -2500.0, '2023-10-10 15:00:00', 'Rent Payment', 'TX011', 2, 1, 5.0),
    (1012, 101, -60.0, '2023-10-11 11:00:00', 'Gas Station', 'TX012', 2, 1, 0.0),
    (1013, 103, -200.0, '2023-10-12 18:30:00',
     'Online Shopping', 'TX013', 2, 1, 0.0),
    (1014, 106, -10.0, '2023-10-13 00:00:00', 'Service Fee', 'TX014', 4, 5, 0.0),
    (1015, 114, 1000.0, '2023-10-14 10:00:00', 'Transfer In', 'TX015', 1, 4, 0.0),
]

atm_data = [
    (1, 1, '2018-01-01', 200000.0, 150000.0,
     1, '2023-09-01', '100 Main St', '10001'),
    (2, 1, '2018-01-01', 200000.0, 12000.0, 1,
     '2023-09-01', '100 Main St (Lobby)', '10001'),
    (3, 2, '2019-05-15', 150000.0, 80000.0, 1,
     '2023-09-15', '250 North Ave', '10020'),
    (4, 2, '2019-05-15', 150000.0, 0.0, 3, '2023-09-15', '45 West Blvd', '10030'),
    (5, 3, '2020-03-20', 100000.0, 95000.0,
     1, '2023-10-01', '78 East Rd', '10040'),
    (6, 1, '2021-06-10', 250000.0, 200000.0, 1,
     '2023-10-05', '1 Terminal Way', '11000'),
    (7, 1, '2021-06-10', 250000.0, 180000.0, 1,
     '2023-10-05', '1 Terminal Way (Gate 5)', '11000'),
    (8, 3, '2022-01-15', 100000.0, 5000.0, 1,
     '2023-08-20', '500 Shop Ln', '10050'),
    (9, 2, '2018-11-11', 150000.0, 75000.0, 2,
     '2023-10-10', '200 Atlantic Ave', '11201'),
    (10, 1, '2019-08-08', 200000.0, 190000.0, 1,
     '2023-09-25', '30 Queens Blvd', '11101'),
    (11, 4, '2020-02-02', 120000.0, 60000.0, 1,
     '2023-09-10', '40 Grand Concourse', '10451'),
    (12, 1, '2021-04-04', 200000.0, 1000.0, 3,
     '2023-10-02', '10 Richmond Rd', '10301'),
    (13, 2, '2017-07-07', 150000.0, 0.0, 4, '2023-10-12', '50 Hudson St', '07030'),
    (14, 3, '2022-09-09', 100000.0, 45000.0,
     1, '2023-10-08', '10 Broad St', '07102'),
    (15, 4, '2023-01-01', 120000.0, 110000.0, 5,
     '2023-10-11', '5 Washington St', '07030'),
]

city_atm_data = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 9), (3, 10), (4, 11), (5, 12), (6, 13), (7, 14), (8, 15),
]

atm_transaction_data = [
    (1004, 1), (1007, 1), (1012, 1),
    (1004, 2), (1007, 2),
    (1004, 3), (1007, 3), (1012, 3),
    (1004, 4), (1007, 4),
    (1004, 5), (1007, 5),
]

bank_acc_promotion_data = [
    (1, 101), (2, 102), (1, 105), (3, 107), (4, 115),
    (2, 108), (5, 101), (3, 103), (1, 112), (4, 113),
    (2, 114), (1, 104), (3, 106), (5, 109), (4, 110),
]

employee_data = [
    (1, 'Alice', 'Cooper', 15, '+15552001', 'a.cooper@bank.com',
     '2015-01-10', None, 75000, 1, 1, 1, 1, 1),
    (2, 'Bob', 'Marley', 12, '+15552002', 'b.marley@bank.com',
     '2016-03-15', None, 62000, 1, 1, 1, 1, 2),
    (3, 'Charlie', 'Chaplin', 13, '+15552003', 'c.chaplin@bank.com',
     '2020-05-20', None, 55000, 2, 1, 2, 1, 2),
    (4, 'Diana', 'Ross', 7, '+15552004', 'd.ross@bank.com',
     '2021-08-01', None, 54000, 1, 1, 1, 2, 2),
    (5, 'Elton', 'John', 9, '+15552005', 'e.john@bank.com',
     '2017-11-30', None, 68000, 3, 1, 3, 1, 3),
    (6, 'Freddie', 'Mercury', 10, '+15552006', 'f.mercury@bank.com',
     '2018-02-14', None, 85000, 3, 1, 3, 3, 4),
    (7, 'George', 'Harrison', 3, '+15552007', 'g.harrison@bank.com',
     '2022-01-10', None, 56000, 3, 1, 3, 2, 2),
    (8, 'Harry', 'Styles', 3, '+15552008', 'h.styles@bank.com',
     '2023-06-15', None, 52000, 3, 1, 3, 4, 2),
    (9, 'Ian', 'McKellen', 14, '+15552009', 'i.mckellen@bank.com',
     '2014-09-01', None, 92000, 3, 1, 3, 7, 1),
    (10, 'Julia', 'Roberts', 4, '+15552010', 'j.roberts@bank.com',
     '2019-04-22', None, 70000, 1, 1, 1, 7, 3),
    (11, 'Kevin', 'Bacon', 9, '+15552011', 'k.bacon@bank.com',
     '2020-10-30', None, 48000, 1, 1, 1, 1, 5),
    (12, 'Liam', 'Neeson', 6, '+15552012', 'l.neeson@bank.com',
     '2019-07-04', '2022-01-01', 51000, 4, 1, 4, 2, 5),
    (13, 'Monica', 'Bellucci', 3, '+15552013', 'm.bellucci@bank.com',
     '2021-03-08', None, 72000, 5, 1, 5, 5, 2),
    (14, 'Nicole', 'Kidman', 2, '+15552014', 'n.kidman@bank.com',
     '2016-12-12', None, 65000, 6, 1, 6, 5, 2),
    (15, 'Amalia', 'Cember', 8, '+15552015', 'o.winfrey@bank.com',
     '2015-05-05', None, 88000, 1, 1, 1, 1, 4),
]

transaction_for_atm_data = [
    (1004, 'Cash Withdrawal'),
    (1007, 'Balance Inquiry'),
    (1012, 'Deposit'),
]

tables_data = [
    ('INSERT INTO Gender (genderId, name) VALUES (%s, %s)', gender_data),
    ('INSERT INTO ClientStatus (clientStatusId, name) VALUES (%s, %s)', client_status_data),
    ('INSERT INTO MainNationality (nationalityId, name) VALUES (%s, %s)',
     main_nationality_data),
    ('INSERT INTO Citizenship (citizenshipId, name) VALUES (%s, %s)', citizenship_data),
    ('INSERT INTO Language (languageId, name) VALUES (%s, %s)', language_data),
    ('INSERT INTO AccountType (typeId, name) VALUES (%s, %s)', account_type_data),
    ('INSERT INTO AccountStatus (statusId, name) VALUES (%s, %s)', account_status_data),
    ('INSERT INTO Currency (currencyId, name) VALUES (%s, %s)', currency_data),
    ('INSERT INTO TransactionType (transactionTypeId, name) VALUES (%s, %s)',
     transaction_type_data),
    ('INSERT INTO TransactionStatus (statusId, name) VALUES (%s, %s)',
     transaction_status_data),
    ('INSERT INTO LoanType (typeId, name) VALUES (%s, %s)', loan_type_data),
    ('INSERT INTO LoanStatus (statusId, name) VALUES (%s, %s)', loan_status_data),
    ('INSERT INTO Promotion (promotionId, name) VALUES (%s, %s)', promotion_data),
    ('INSERT INTO Region (regionId, name) VALUES (%s, %s)', region_data),
    ('INSERT INTO ATMStatus (statusId, name) VALUES (%s, %s)', atm_status_data),
    ('INSERT INTO Brand (brandId, name) VALUES (%s, %s)', brand_data),
    ('INSERT INTO TransactionForATM (transactionId, name) VALUES (%s, %s)',
     transaction_for_atm_data),
    ('INSERT INTO CountryOfEmployment (countryOfEmploymentId, name) VALUES (%s, %s)',
     country_of_employment_data),
    ('INSERT INTO `Position` (positionId, name) VALUES (%s, %s)', position_data),
    ('INSERT INTO Department (departmentId, name, phone, dateCreated, email, regionId) VALUES (%s, %s, %s, %s, %s, %s)', department_data),
    ('INSERT INTO City (cityId, name, regionId) VALUES (%s, %s, %s)', city_data),
    ('INSERT INTO Branch (branchId, name, address, postalCode, cityId, dateOpened, phone, departmentId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', branch_data),
    ('INSERT INTO BranchDepartment (branchId, departmentId) VALUES (%s, %s)',
     branch_department_data),
    ('INSERT INTO Customer (customerId, firstName, lastName, dateOfBirth, genderId, street, postalCode, phone, email, dateJoined, nationalityId, citizenshipId, clientStatusId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', customer_data),
    ('INSERT INTO Identification (identificationId, customerId, identificationTypeId, identificationNumber, dateIssued, dateExpired) VALUES (%s, %s, %s, %s, %s, %s)', identification_data),
    ('INSERT INTO BankAccount (accountId, customerId, typeId, balance, dateCreated, creditScore, currencyId, languageId, statusId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', bank_account_data),
    ('INSERT INTO Loan (loanId, accountId, typeId, amount, startDate, finishDate, statusId) VALUES (%s, %s, %s, %s, %s, %s, %s)', loan_data),
    ('INSERT INTO Transaction (transactionId, accountId, amount, dateTime, description, code, transactionTypeId, statusId, fee) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', transaction_data),
    ('INSERT INTO ATM (atmId, brandId, dateInstalled, cashCapacity, currentCashAmount, statusId, maintenanceDate, address, postalCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', atm_data),
    ('INSERT INTO CityATM (cityId, atmId) VALUES (%s, %s)', city_atm_data),
    ('INSERT INTO ATMTransaction (transactionId, atmId) VALUES (%s, %s)',
     atm_transaction_data),
    ('INSERT INTO BankAccPromotion (promotionId, accountId) VALUES (%s, %s)',
     bank_acc_promotion_data),
    ('INSERT INTO Employee (employeeId, firstName, lastName, positionId, phone, email, dateHired, dateLeft, salary, nationalityId, countryOfEmploymentId, citizenshipId, branchId, departmentId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', employee_data),
]

total_inserted = 0

for sql, data_list in tables_data:
    for data in data_list:
        try:
            mycursor.execute(sql, data)
            total_inserted += 1
        except Exception as e:
            pass

mydb.commit()

print(f"Total rows inserted: {total_inserted}")

mydb.close()
