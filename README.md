# silent-auction

A real-time Silent Auction Application built with Flask to facilitate online bidding for items in a seamless and interactive way. This application is designed for efficiency, security, and user engagement, providing a dynamic platform for auctioneers and bidders.

---

## **Silent Auction Application**

A dynamic and interactive web-based **Silent Auction Application** built with **Flask**, designed to facilitate online bidding with real-time updates and an intuitive user experience.

---

## **Features**

- **Real-Time Bidding**: Instant updates for all participants using WebSocket technology.
- **Auction Management**: Admin tools to create, update, and manage auction items.
- **Countdown Timers**: Live timers for each auction item, ensuring timely bidding.
- **Email Notifications**: Automatic notifications for auction winners.
- **Secure Bidding**: Robust validation to ensure bid integrity.
- **User-Friendly Interface**: Simple and elegant design for all users.

---

## **Tech Stack**

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-SocketIO
- **Frontend**: HTML, JavaScript, CSS
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Heroku with Gunicorn

---

## **Getting Started**

### **Prerequisites**

- Python 3.9 or higher
- Pip or Conda package manager
- Git

### **Installation**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/gareytwin1/silent-auction.git
   cd silent-auction
   ```

2. **Create a Virtual Environment**:

   Using `conda`:

   ```bash
   conda env create -f environment.yml
   conda activate sa_env
   ```

   Using `venv`:

   ```bash
   python -m venv sa_env
   ```

   - On macOS/Linux:

   ```bash
   source sa_env/bin/activate
   ```

   - On Windows:

   ```bash
   sa_env\Scripts\activate
   ```

   - Confirm activation: The prompt will change to show the virtual environment's name  (sa_env)

   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

### **For Bidders**

1. Register or log in to the platform.
2. Browse active auction items.
3. Place bids in real-time, ensuring they are higher than the current highest bid.
4. Receive email notifications if you win an item.

### **For Admins**

1. Log in with admin credentials.
2. Add, update, or remove auction items.
3. Monitor live bids and finalize auctions.

---


## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## **Contact**

For questions or feedback, please contact:

- **Email**: <gareytwin1@gmail.com>
- **GitHub**: [gareytwin1](https://github.com/gareytwin1)

---

## **Future Enhancements**

- **Payment Integration**: Add payment gateways for seamless transactions.
- **Analytics Dashboard**: Provide real-time statistics for admins.
- **Mobile Optimization**: Ensure the application works flawlessly on mobile devices.

---