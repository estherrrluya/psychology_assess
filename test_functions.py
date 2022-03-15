"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""
import pytest
from classes import PatientsInfo

@pytest.fixture
def patients_info():
    return PatientsInfo()

def test_disease_cat(patients_info):

    assert callable(patients_info.disease_cat)
    assert type(patients_info.disease_cat('Anxiety', 3)) == tuple
    assert patients_info.disease_cat('Anxiety', 3) == ([{'disease_name': 'Anxiety', 'duration_illness': 3}, {'disease_name': 'Anxiety', 'duration_illness': 3}], {'number_anxiety': 2, 'number_depression': 0})
    
def test_urgent_care(patients_info):
    
    symptoms = ['feeling_restless', 'fatigue', 'sleep_issues']

    assert callable(patients_info.urgent_care)
    assert type(patients_info.urgent_care('Anxiety', 4, symptoms)) == str
    assert patients_info.urgent_care('Anxiety', 4, symptoms) == 'Can take melatonin supplements or sleeping pills'

def test_treatment(patients_info):
    
    assert callable(patients_info.treatment)
    assert type(patients_info.treatment('Anxiety', 'Pharmacotherapy')) == str
    assert patients_info.treatment('Anxiety', 'Pharmacotherapy') == 'Lexapro-Escitalopram'
    assert patients_info.treatment('Anxiety', 'Therapy') == 'Your preference must either be Psychotherapy or Pharmcotherapy'
    



                 
    