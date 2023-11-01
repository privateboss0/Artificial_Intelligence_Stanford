import time
import pyotp
import qrcode

secretkey = "PublicPrivate"

# Counter variable to track the number of failed OTP attempts.
counter = 0

# Create a TOTP object.
totp = pyotp.TOTP(secretkey)

while True:
  
  otp_code = input("Enter the OTP from your Google Authenticator App: ")

  # Verify the OTP with secretkey.
  if totp.verify(otp_code):
    # Reset the counter variable.
    counter = 0

    # Authentication was successful.
    print("Authentication successful!")

     # Make the API call.
    #Implement the API call here.


    break
  else:
    # Increment the counter variable.
    counter += 1
    
    print("Authentication failed, Please try again!")

   
    if counter == 5:
      
      # Prompt the user to enter a recovery code after 5 failed OTP attempt by importing Recovery_Code_App
      import Recovery_Code_App
      
      recovery_code = input("Enter your recovery code: ")

      # Verify the recovery code.
      hotp = pyotp.HOTP(secretkey)
      if hotp.verify(recovery_code):
        
        # Reset the counter variable and authentication process.
        counter = 0

        print("Authentication successful!")
        break
      else:

        print("Invalid recovery code. We advise to contact Support after 10 trials")