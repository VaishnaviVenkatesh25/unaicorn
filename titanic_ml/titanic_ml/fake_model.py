def fake_prediction(user_age):
    if user_age>10:
        prediction="survived( Over 10 )"
    else:
        prediction="Super Survived (Under 10)"
    return prediction
