def calculate_interest(balance,interest,days) :
    """
    Calculates interest on a given balance. The key arguments are
    1. Balance  - Amount on which balance needs to be calculated
    2. Interest - Annual interest in percentage
    3. Days     - Number of days since the beginning of the year
    """
    interest_amount = balance * ( interest / 100 ) * ( days/365 )
    return interest_amount

calculate_interest.