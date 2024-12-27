# import streamlit as st
# import gspread
# from google.oauth2.service_account import Credentials

# # Set up the credentials for accessing Google Sheets
# scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.readonly"]
# # creds = Credentials.from_service_account_file(
# #     r'C:\Users\sanja\OneDrive\Desktop\DAV Database\myfirst-434417-56e48925530b.json',
# #     scopes=scopes
# # )
# # client = gspread.authorize(creds)



# # Load credentials from Streamlit secrets
# credentials_dict = st.secrets["google_credentials"]

# # Create the credentials object from the secrets
# creds = Credentials.from_service_account_info(credentials_dict, scopes=scopes)

# # Authorize the client
# client = gspread.authorize(creds)

# # The ID of your Google Sheet (from the URL)
# sheet_id = '1x9Lbbmh5zY1LOa801o7B4i0c8gOTE53A37pd_doI3ek'
# sheet = client.open_by_key(sheet_id)

# # Set up Streamlit app
# st.title("Alumni Data Entry Portal")
# st.markdown("Welcome to the Alumni Data Entry Portal. Please enter your details.")

# # Initialize session_state variables
# if 'password_entered' not in st.session_state:
#     st.session_state['password_entered'] = False
# if 'user_details' not in st.session_state:
#     st.session_state['user_details'] = {}
# if 'selected_profession' not in st.session_state:
#     st.session_state['selected_profession'] = None
# if 'headers' not in st.session_state:
#     st.session_state['headers'] = []


# password = st.text_input("Enter Password to Proceed", type="password")

# if password == "dav":
#     st.session_state['password_entered'] = True
# else:
#     if password != "" and not st.session_state['password_entered']:
#         st.error("Incorrect password. Please try again.")


# if st.session_state['password_entered']:
#     st.success("Password Correct! You can now enter your details.")
    
#     # Get the list of sheet names (for example, "Doctor", "Alumni")
#     sheet_names = ['Doctors','Engineers', 'Psychologists', 'Real Estate Agents', 'Investment Bankers', 'Analysts', 'Salesman', 'Teachers', 'Lawyers', 'Architects', 'Others']  # Modify this list based on your actual sheet names

#     # Create a dropdown for selecting the profession
#     selected_profession = st.selectbox("Select your Profession", sheet_names)

#     if selected_profession != st.session_state['selected_profession']:
#         st.session_state['selected_profession'] = selected_profession
#         # Get the corresponding sheet based on the selected profession
#         selected_sheet = sheet.worksheet(st.session_state['selected_profession'])

#         # Get the headers (columns) from the selected sheet
#         st.session_state['headers'] = selected_sheet.row_values(1)  # Assuming the first row has the column names

#     if st.session_state['headers']:
#             # First collect Name
#         st.session_state['user_details']["Name"] = st.text_input("Enter your Name", value=st.session_state['user_details'].get("Name", ""))
        
#         # Then collect the other details in the correct order as per the sheet headers
#         for header in st.session_state['headers'][1:]:  # Skip the first column ("Name")
#             st.session_state['user_details'][header] = st.text_input(f"Enter {header}", value=st.session_state['user_details'].get(header, ""))
        
#     # Submit button
#     submit_button = st.button("Submit")
    
#     if submit_button:
#          # If submit button is clicked, add the data to the sheet
#         if all(value != "" for value in st.session_state['user_details'].values()):
#             # Prepare the data as a list for appending to the sheet in the correct order
#             row_data = [st.session_state['user_details'].get(header, "") for header in st.session_state['headers']]
            
#             # Append the data to the corresponding sheet
#             selected_sheet = sheet.worksheet(st.session_state['selected_profession'])
#             selected_sheet.append_row(row_data)
            
#             # Clear user_details so it doesn't carry over on next user submission
#             st.session_state['user_details'] = {}

#             # Show a success message
#             st.success("Thank you for your valuable time! Your details have been submitted successfully.")
#         else:
#              st.error("Please fill in all the fields before submitting.")






import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Set up the credentials for accessing Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.readonly"]

# Load credentials from Streamlit secrets
credentials_dict = st.secrets["google_credentials"]

# Create the credentials object from the secrets
creds = Credentials.from_service_account_info(credentials_dict, scopes=scopes)

# Authorize the client
client = gspread.authorize(creds)

# The ID of your Google Sheet (from the URL)
sheet_id = '1x9Lbbmh5zY1LOa801o7B4i0c8gOTE53A37pd_doI3ek'
sheet = client.open_by_key(sheet_id)

# Set up Streamlit app
st.title("Alumni Data Entry Portal")
st.markdown("Welcome to the Alumni Data Entry Portal. Please enter your details.")

# Initialize session_state variables
if 'password_entered' not in st.session_state:
    st.session_state['password_entered'] = False
if 'user_details' not in st.session_state:
    st.session_state['user_details'] = {}
if 'selected_profession' not in st.session_state:
    st.session_state['selected_profession'] = None
if 'headers' not in st.session_state:
    st.session_state['headers'] = []

password = st.text_input("Enter Password to Proceed", type="password")

if password == "dav":
    st.session_state['password_entered'] = True
else:
    if password != "" and not st.session_state['password_entered']:
        st.error("Incorrect password. Please try again.")

if st.session_state['password_entered']:
    st.success("Password Correct! You can now enter your details.")
    
    # Get the list of sheet names (for example, "Doctor", "Alumni")
    sheet_names = ['Doctors','Engineers', 'Psychologists', 'Real Estate Agents', 'Investment Bankers', 'Analysts', 'Salesman', 'Teachers', 'Lawyers', 'Architects', 'Others']  # Modify this list based on your actual sheet names

    # Create a dropdown for selecting the profession
    selected_profession = st.selectbox("Select your Profession", sheet_names)

    if selected_profession != st.session_state['selected_profession']:
        st.session_state['selected_profession'] = selected_profession
        # Get the corresponding sheet based on the selected profession
        selected_sheet = sheet.worksheet(st.session_state['selected_profession'])

        # Get the headers (columns) from the selected sheet
        st.session_state['headers'] = selected_sheet.row_values(1)  # Assuming the first row has the column names

    if st.session_state['headers']:
            # First collect Name
        st.session_state['user_details']["Name"] = st.text_input("Enter your Name", value=st.session_state['user_details'].get("Name", ""))
        
        # Then collect the other details in the correct order as per the sheet headers
        for header in st.session_state['headers'][1:]:  # Skip the first column ("Name")
            st.session_state['user_details'][header] = st.text_input(f"Enter {header}", value=st.session_state['user_details'].get(header, ""))
        
    # Submit button
    submit_button = st.button("Submit")
    
    if submit_button:
        # Prepare the data as a list for appending to the sheet in the correct order
        row_data = [st.session_state['user_details'].get(header, "") for header in st.session_state['headers']]
        
        # Append the data to the corresponding sheet
        selected_sheet = sheet.worksheet(st.session_state['selected_profession'])
        selected_sheet.append_row(row_data)
        
        # Clear user_details so it doesn't carry over on next user submission
        st.session_state['user_details'] = {}

        # Show a success message
        st.success("Thank you for your valuable time! Your details have been submitted successfully.")
