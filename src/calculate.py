#!/usr/bin/env python3
"""
Cancer Risk Calculator - Core calculation logic.
"""

def calculate_risk_score(age, pack_years, age_first_cigarette):
    """
    Calculate estimated lung cancer risk score based on smoking-related variables.
    
    Parameters:
    age (int): Current age of the individual
    pack_years (float): Pack-years of smoking (packs per day * years smoked)
    age_first_cigarette (int): Age at first cigarette consumption
    
    Returns:
    float: Risk score (higher indicates higher risk)
    
    Raises:
    ValueError: If any input is invalid (negative age, pack_years, or age_first_cigarette)
    """
    # Input validation
    if age <= 0:
        raise ValueError("Age must be positive")
    if pack_years < 0:
        raise ValueError("Pack-years cannot be negative")
    if age_first_cigarette <= 0:
        raise ValueError("Age of first cigarette must be positive")
    
    # Simple risk model: risk increases with pack-years and earlier smoking initiation
    # Base risk factor
    base_risk = pack_years * 0.5
    
    # Early initiation penalty: the younger the age of first cigarette, the higher the risk
    if age_first_cigarette < 18:
        early_initiation_penalty = 2.0 * (18 - age_first_cigarette)
    elif age_first_cigarette < 25:
        early_initiation_penalty = 1.0 * (25 - age_first_cigarette)
    else:
        early_initiation_penalty = 0.0
    
    # Age factor: risk increases with age
    age_factor = age * 0.1
    
    # Total risk score
    risk_score = base_risk + early_initiation_penalty + age_factor
    
    return risk_score

if __name__ == "__main__":
    # Example usage
    age = 45
    pack_years = 20.5
    age_first_cigarette = 16
    score = calculate_risk_score(age, pack_years, age_first_cigarette)
    print(f"Estimated lung cancer risk score: {score:.2f}")