# BloodLink-BAIUST

BloodLink-BAIUST is a web application designed to facilitate blood requests among students of BAIUST (Bangladesh Army International University of Science and Technology). The platform allows registered students to both donate blood and request blood when needed.

## Features

- **User Registration**: Only BAIUST students can register on the platform.
- **Blood Donation and Request**: Every registered user can both donate blood and request blood when necessary.
- **Eligibility Check**: Before sending out blood request notifications, the system checks whether a student is eligible to donate blood.
- **Notification System**: When a blood request is made, details of the requestor are sent to all users after eligibility verification.
- **Confirmation via Email**: If a student agrees to donate blood, the donor's information is sent to the requestor via email.

## Technologies Used

- **Flask**: Flask is used as the web framework.
- **Flask-Login**: For user authentication and session management.
- **Flask-Mail**: For sending email notifications.
- **Flask-Migrate**: For handling database migrations.
- **Flask-SQLAlchemy**: Flask extension for SQLAlchemy, used for database management.
- **Flask-WTF**: For form handling and validation.
- **Alembic**: Database migration tool.
- **Blinker**: For signaling support in Flask.
- **Click**: Command line interface creation kit.
- **Jinja2**: Template engine for Flask.
- **Werkzeug**: WSGI utility library for Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapper.
- **python-dotenv**: For managing environment variables.
- **WTForms**: Library for form creation and validation.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/BloodLink-BAIUST.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    - Create a `.env` file in the root directory.
    - Add necessary environment variables like database URL, email configuration, etc.

4. Run the application:

    ```bash
    flask run
    ```

## Usage

1. Navigate to the application URL in your web browser.
2. Register as a student of BAIUST.
3. Log in to your account.
4. Choose whether to donate blood or request blood as per your requirement.
5. If you request blood, wait for donors to respond. Once a donor agrees, their information will be sent to you via email.
6. If you agree to donate blood, confirm your donation, and your information will be sent to the requester.

## Contributors

- Md Khaled Bin Joha, Md Shamiul Haque Upom

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.
