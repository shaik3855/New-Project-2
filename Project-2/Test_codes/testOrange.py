from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Orange_Data
from Test_Locators.locators import Orange_Locators
from selenium.webdriver.common.keys import Keys
import pytest

class Test_OrangeHRM:

    #Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.quit()
   
    def test_get_title(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.get(Orange_Data().url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Web Title Captured")

    def test_TC_PIM_01(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click()

        # Click on the "search_bar" locator
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
        # Enter on the search_bar "a" element
        search_box = self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator)
        search_box.send_keys(Orange_Locators.a)
        # Searchbutton text display A
        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
        search_box.send_keys(Orange_Locators.b)
        # Searchbutton text display B
        
        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
       
        search_box.send_keys(Orange_Locators.c)
        # Searchbutton text display C
       
        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
      
        search_box.send_keys(Orange_Locators.d)
        # Searchbutton text display D
       
        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
       
        search_box.send_keys(Orange_Locators.e)
        # Searchbutton text display E

        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
     
        search_box.send_keys(Orange_Locators.f)
        # Method - Searchbutton text display F
  
        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
 
        search_box.send_keys(Orange_Locators.g)
        # Searchbutton text display G
     
        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
    
        search_box.send_keys(Orange_Locators.h)
        # Searchbutton text display H

        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
       
        search_box.send_keys(Orange_Locators.i)
        # Searchbutton text display I
        
        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
        
        search_box.send_keys(Orange_Locators.j)
        # Searchbutton text display J
        
        search_box.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        # Search box cleared
        
        search_box.send_keys(Orange_Locators.k)
        # Searchbutton text display K
        assert self.driver.title =='OrangeHRM'
        print('The user should be able to see Admin Page Menu and Idividual Menu Name displayed under Search Text box')

    def test_TC_PIM_02(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click()    
        # Click on the "admin_button" locator
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.admin_button).click()
        # Click on the "user_management_header" locator
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.user_management_header).click()
     
        # Click on the "users_button" locator
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.users_button).click()
        # Click on the "user_role_dropdown" locator
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.userrole_dropdown).click()
        # Select from the dropdown "Admin" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Admin).click()
       
        # Click on the "status_dropdown" locator
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.status_dropdown).click()
        # Select from the dropdown "Enabled" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Enabled).click()
        # Select from the dropdown "user_role_dropdown" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.userrole_dropdown).click()
        # Select from the dropdown "ESS" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.ESS).click()
        # Click on the "status_dropdown" locator
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.status_dropdown).click()
        # Select from the dropdown "Enabled" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Disabled).click()
        assert self.driver.title =='OrangeHRM'
        print('The user should be able to see admin, Enabled, ESS, Disabled values in drop down')

        
    def test_TC_PIM_03(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "Add Employee" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.add_employee_button).click()
        
        # Enter the employee's first name, middle name, and last name
        self.driver.find_element(by=By.NAME, value=Orange_Locators.first_name_locator).send_keys(Orange_Locators.first_name)
        self.driver.find_element(by=By.NAME, value=Orange_Locators.middle_name_locator).send_keys(Orange_Locators.middle_name)
        self.driver.find_element(by=By.NAME, value=Orange_Locators.last_name_locator).send_keys(Orange_Locators.last_name)
        
        # Click on the "Radio button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.radio_button_1).click()
        
        # Enter the employee's user name, password, confirmed password, and save
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.username_01).send_keys(Orange_Locators.username_field)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.password_01).send_keys(Orange_Locators.password_field)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.confirm_password).send_keys(Orange_Locators.password_field_2)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.save_button_2).click()
        assert self.driver.title =='OrangeHRM'
        print('The user should able to see the page moved to "Empolyee list" once user created') 

    def test_TC_PIM_04(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click()
        
        # Click on the "Personal_Details button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Personal_Details).click()
        # Click on the "Contact_Details button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Contact_Details).click()
        # Click on the "Emergency_Contacts button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Emergency_Contacts).click()
        # Click on the "Dependents button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Dependents).click()
        # Click on the "Immigration button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Immigration).click()
        # Click on the "Job button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Job).click()
        # Click on the "Salary button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Salary).click()
        # Click on the "TaxExemptions button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.TaxExemptions).click()
        # Click on the "Immigration button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Report_to).click()
        # Click on the "Qualifications button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Qualifications).click()
        # Click on the "Memberships button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Memberships).click()
        assert self.driver.title =='OrangeHRM'
        print('The user should able to see all the tabs present in Employee list page ')

    def test_TC_PIM_05(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click()
        
        # Click on the "Personal_Details"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Personal_Details).click()
        # Click on the "Driver's License And Enter the Number"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Driving_License_field).send_keys(Orange_Locators.Driving_License_Number)
        
        # Click on the "License Expiry And Enter the Date"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Driving_License_Expiry).send_keys(Orange_Locators.Driving_License_ExpiryDate)
       
        # Click on the "Nationality_Dropdown and Select the Country"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Nationality_Dropdown).send_keys(Orange_Locators.Indian_Select)

        # Click on the "Marital_Status_field and Select the Marital_Status_Select_Button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Marital_Status_field).send_keys(Orange_Locators.Marital_Status_Select_Button)

        # Click on the "DateofBirth_locator and Enter the DateofBirth_field"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.DateofBirth_locator).send_keys(Orange_Locators.DateofBirth_field)
     
        # Click on the "Gender_button and Select "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Gender_button).click()
   
        # Click on the "Military_Service and Enter the Military_field"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Military_Service).send_keys(Orange_Locators.Military_field)
   
        # Click on the "save_button_3"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.save_button_3).click()
        assert self.driver.title =='OrangeHRM'
        print('The user Should able to see all the filled details present in personal Detail page')

    def test_TC_PIM_06(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click()   
        
        # Click on the "Contact_Details"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Contact_Details).click()
               
        # Click on the "Street_01 and Enter The Address"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Street_01).send_keys(Orange_Locators.street_1)
        
        # Click on the "Street_02 and Enter The Address"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Street_02).send_keys(Orange_Locators.street_2)
      
        # Click on the "City and Enter The Address"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.City).send_keys(Orange_Locators.city)
               
        # Click on the "Country_locator and Select The Country_Selector"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Country_locator).send_keys(Orange_Locators.Country_Selector)
      
        # Click on the "Telephone and Enter The Number"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Telephone).send_keys(Orange_Locators.Home_Phone)
    
        # Click on the "Mobile and Enter The Number"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Mobile).send_keys(Orange_Locators.Mobile_Phone)
       
        # Click on the "Work and Enter The Profession"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Work).send_keys(Orange_Locators.Profession)
      
        # Click on the "Email and Enter The Emailaddress"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Email).send_keys(Orange_Locators.Work_email)
      
        # Click on the "save_button_4 and Save"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.save_button_4).click()
        assert self.driver.title =='OrangeHRM'
        print('The user Should be able to see all the filled details present in Contact Detail page')
        
    def test_TC_PIM_07(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click()       
        # Click on the "Emergency_Contacts"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Emergency_Contacts).click()
        
        # Click on the "Add_button_1"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Add_button_1).click()
        
        # Click on the "Relation_Name and Enter The Name"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Relation).send_keys(Orange_Locators.Relation_Name)
      
        # Click on the "RelationShip and Enter The Relation"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.RelationShip).send_keys(Orange_Locators.Relation_with)
        
        # Click on the "Telephone_01 and Enter The Number"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Telephone_01).send_keys(Orange_Locators.Home_Phone_01)
       
        # Click on the "Mobile_01 and Enter The Number"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Mobile_01).send_keys(Orange_Locators.Mobile_Phone_01)
               
        # Click on the "save_button_5 and Save"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.save_button_5).click()
        assert self.driver.title =='OrangeHRM'
        print('The user Should be able to see all the filled details present in Emergency Contacts page')

    def test_TC_PIM_08(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click() 

        # Click on the "Dependents"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Dependents).click()
           
        # Click on the "Add_button_2"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Add_button_2).click()
  
        # Click on the "Dependent and Enter The Dependent_Name"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Dependent).send_keys(Orange_Locators.Dependent_Name)
        # Click on the "Relation_Dropdown and Selct The other option"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Relation_Dropdown).send_keys(Orange_Locators.Relation_Option)

        # Click on the "DOB and Enter The DOB_field"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.DOB).send_keys(Orange_Locators.DOB_field)
        
        # Click on the "save_button_6 and Save"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.save_button_6).click()
        assert self.driver.title =='OrangeHRM'
        print('The user Should be able to see all the filled details present in Dependents page')     

    def test_TC_PIM_09(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click()
        # Click on the "Job"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Job).click()
               
        # Click on the "Joined_Locator and Enter theJoined_Date "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Joined_Locator).send_keys(Orange_Locators.Joined_Date)
     
        # Click on the "Job_Title and Enter the Profession "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Job_Title).send_keys(Orange_Locators.Profession)
      
        # Click on the "Job_Category and Enter the Category_profession "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Job_Category).send_keys(Orange_Locators.Category_profession)
        
        # Click on the "Sub_Unit and Enter the Sub_Unit_Profession "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Sub_Unit).send_keys(Orange_Locators.Sub_Unit_Profession)
       
        # Click on the "Location_Locator and Enter the Location_tab "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Location_Locator).send_keys(Orange_Locators.Location_tab)
       
        # Click on the "Employee_Status_Locator and Enter the Employee_Status "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Employee_Status_Locator).send_keys(Orange_Locators.Employee_Status)
       
        # Click on the "Contact_Details_button "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Contact_Details_button).click()
        
        # Click on the "Cotract_Start and Enter the Cotract_Start_date "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Cotract_Start).send_keys(Orange_Locators.Cotract_Start_date)
       
        # Click on the "Cotract_End and Enter the Cotract_End_date "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Cotract_End).send_keys(Orange_Locators.Cotract_End_date)
        # Click on the "save_button_7 "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.save_button_7).click()
        assert self.driver.title =='OrangeHRM'
        print('The user should be able to see all the filled details present in Job details page')  

    def test_TC_PIM_10(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click()  
        # Click on the "Job"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Job).click()
        
       # Click on the "Employee_Termination"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Employee_Termination).click()
      
        # Click on the "Date_Locator and Enter the Date "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Date_Locator).send_keys(Orange_Locators.Termination_Date)
        
        # Click on the "Reason_Locator and Enter the Termination_Reason "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Reason_Locator).send_keys(Orange_Locators.Termination_Reason)
        
        # Click on the "Note_Locator and Enter the Note "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Note_Locator).send_keys(Orange_Locators.Note)
                
        # Click on the "save_button_8 "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Save_button_8).click()
        assert self.driver.title =='OrangeHRM'
        print('The user should be able to see Termination on Job details page') 

    def test_TC_PIM_11(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click() 
        # Click on the "Job"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Job).click()
       
       # Click on the "Activate_Termination"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Activate_Termination).click()
        assert self.driver.title =='OrangeHRM'
        print('The user should be able to see Activation on Job details page') 

    def test_TC_PIM_12(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click()  

        # Click on the "Salary_Button"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Salary).click()
       
        # Click on the "Add_button_3"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Add_button_3).click()
        
        # Click on the "Salary_Locator and Enter the Salary "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Salary_Locator).send_keys(Orange_Locators.Salary_1)
        
        # Click on the "Pay_Grade_Locator and Enter the Pay_Grade "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Pay_Grade_Locator).send_keys(Orange_Locators.Pay_Grade)
        
        # Click on the "Pay_Frequency_Locator and Enter the Pay_Frequency "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Pay_Frequency_Locator).send_keys(Orange_Locators.Pay_Frequency)
       
        # Click on the "Currency_Locator and Enter the Currency "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Currency_Locator).send_keys(Orange_Locators.Currency)
      
        # Click on the "Amount_Locator and Enter the Amount "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Amount_Locator).send_keys(Orange_Locators.Amount)
        
        # Click on the "Save_button_9"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Save_button_9).click()
        assert self.driver.title =='OrangeHRM'
        print('The user should be able to see Salary and Deposit on Salary details page')  

    def test_TC_PIM_13(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click() 
        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()
       
        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()
        
        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)
      
        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
     
        # Click on the "ID"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.id_locator).click()
        # Click on the "TaxExemptions"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.TaxExemptions).click()
             
        # Click on the "Status_Locator and Enter the Status "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Status_Locator).send_keys(Orange_Locators.Status)
        # Click on the "Examptions_Locator and Enter the Examptions "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Examptions_Locator).send_keys(Orange_Locators.Examptions)
    
        # Click on the "State_Locator and Enter the State "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.State_Locator).send_keys(Orange_Locators.State)
      
        # Click on the "Status_Locator_1 and Enter the Status_1 "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Status_Locator_1).send_keys(Orange_Locators.Status_1)
      
        # Click on the "Examptions_Locator_1 and Enter the Examptions_1 "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Examptions_Locator_1).send_keys(Orange_Locators.Examptions_1)
      
        # Click on the "Un_Employeement_Locator and Enter the Un_Employeement_State "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Un_Employeement_Locator).send_keys(Orange_Locators.Un_Employeement_State)
  
        # Click on the "Work_State_Locator and Enter the Work_State "
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Work_State_Locator).send_keys(Orange_Locators.Work_State)
   
        # Click on the "Save_button_10"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.Save_button_10).click()
        assert self.driver.title =='OrangeHRM'
        print('The user should be able to see Salary and Deposit on Salary details page') 

            
                 
