from app.database.connection import connection


def insert_customer(customer):
    cursor = connection.cursor()

    query = """
    INSERT INTO customers(
        gender,
        senior_citizen,
        partner,
        dependents,
        tenure_months,
        phone_service,
        multiple_lines,
        internet_service,
        online_security,
        online_backup,
        device_protection,
        tech_support,
        streaming_tv,
        streaming_movies,
        contract,
        paperless_billing,
        payment_method,
        monthly_charges,
        total_charges
    )
    VALUES(
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    RETURNING customer_id;
    """

    cursor.execute(query, (
        customer.gender,
        customer.senior_citizen,
        customer.partner,
        customer.dependents,
        customer.tenure_months,
        customer.phone_service,
        customer.multiple_lines,
        customer.internet_service,
        customer.online_security,
        customer.online_backup,
        customer.device_protection,
        customer.tech_support,
        customer.streaming_tv,
        customer.streaming_movies,
        customer.contract,
        customer.paperless_billing,
        customer.payment_method,
        customer.monthly_charges,
        customer.total_charges
    ))

    customer_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()

    return customer_id
def get_all_customers():
    cursor = connection.cursor()

    query = """
    SELECT * FROM customers
    ORDER BY customer_id;
    """

    cursor.execute(query)

    customers = cursor.fetchall()

    cursor.close()

    return customers
def update_customer(customer_id, customer):
    cursor = connection.cursor()

    query = """
    UPDATE customers
    SET
        gender = %s,
        senior_citizen = %s,
        partner = %s,
        dependents = %s,
        tenure_months = %s,
        phone_service = %s,
        multiple_lines = %s,
        internet_service = %s,
        online_security = %s,
        online_backup = %s,
        device_protection = %s,
        tech_support = %s,
        streaming_tv = %s,
        streaming_movies = %s,
        contract = %s,
        paperless_billing = %s,
        payment_method = %s,
        monthly_charges = %s,
        total_charges = %s
    WHERE customer_id = %s;
    """

    cursor.execute(query, (
        customer.gender,
        customer.senior_citizen,
        customer.partner,
        customer.dependents,
        customer.tenure_months,
        customer.phone_service,
        customer.multiple_lines,
        customer.internet_service,
        customer.online_security,
        customer.online_backup,
        customer.device_protection,
        customer.tech_support,
        customer.streaming_tv,
        customer.streaming_movies,
        customer.contract,
        customer.paperless_billing,
        customer.payment_method,
        customer.monthly_charges,
        customer.total_charges,
        customer_id
    ))

    connection.commit()
    cursor.close()
def delete_customer(customer_id):
    cursor = connection.cursor()

    query = """
    DELETE FROM customers
    WHERE customer_id = %s;
    """

    cursor.execute(query, (customer_id,))

    connection.commit()
    cursor.close()    
def save_prediction(customer_id, prediction, probability, risk_level):

    cursor = connection.cursor()

    query = """
    INSERT INTO predictions (
        customer_id,
        churn_prediction,
        churn_probability,
        risk_level
    )
    VALUES (%s, %s, %s, %s);
    """

    cursor.execute(
        query,
        (customer_id, prediction, probability, risk_level)
    )

    connection.commit()
    cursor.close()  