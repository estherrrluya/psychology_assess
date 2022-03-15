"""Classes used throughout project"""

class PatientsInfo():
    
    """A class that contains method in storing and assessing the patients' conditions.
    
    Parameters
    ----------
    self.duration : list
        Store the patient's disease name and number of years of being illed.
    self.n_anxiety : int
        Count the number of patients that have Anxiety.
    self.n_depression: int
        Count the number of patients that have Depression.
    """ 
    
    def __init__(self):
        
        self.duration = []
        self.n_anxiety = 0
        self.n_depression = 0
        
    def disease_cat(self, disease_name, duration):
        """Store the patients's disease_name, duration of illnesses, and the number of each illnesses in a tuple.
        
        Parameters
        ----------
        disease_name : str
            The name of the disease.
        duration : int
            The duration of illnesses in years.

        Returns
        -------
        self.duration : list
            Patient's disease name and the number of duration.
        {'number_anxiety' : self.n_anxiety,
        'number_depression' : self.n_depression} : dict
            The total number of each illnesses.
        """
        
        #storing the patients' disease name and the duration of illness in a list
        self.duration.append({'disease_name' : disease_name, 
                              'duration_illness' : duration})
        
        #storing the total number of each illnesses that the patients have so far
        if disease_name == 'Anxiety':
            self.n_anxiety += 1
     
        elif disease_name == 'Depression':
            self.n_depression += 1
        
        return self.duration, {'number_anxiety' : self.n_anxiety, 
                               'number_depression' : self.n_depression}
    
    def urgent_care(self, disease_name, duration, symptoms):
        """Determine whether the patients need urgent care or not depending on its duration of illnesses and symptoms
        
        Parameters
        ----------
        disease_name : str
            The name of the disease.
        duration : int
            The duration of illnesses in years.
        symptoms : list
            The list of symptoms that the patients have

        Returns
        -------
        output : str
            The statement saying the care that the patients needed
        """
        
        output = ''
        
        #determine if the patients need urgent care or not
        if len(symptoms) >= 4 and duration >= 3:
            #specific care for specific symptom
            if 'difficulty_concentrating' in symptoms:
                output = 'Can have some medical interventions'
            
            else:
                output = 'Urgent care is needed for this patients with ' + disease_name
            
        else:
            #specific care for specific symptom
            if 'sleep_issues' in symptoms:
                output = 'Can take melatonin supplements or sleeping pills'
            
            else:
                output = 'Urgent care is not needed for this patients with ' + disease_name
        
        return output
    
    def treatment(self, disease_name, preference):
        """Determine what specific treatment the patients should receive according to their preferences.
        
        Parameters
        ----------
        disease_name : str
            The name of the disease.
        preference : str
            Either psychotherapy or pharmacotherapy
            
        Returns
        -------
        rec : str
            The specific recommandations for the patients
        """       
        
        #for different disease, different treatment is recommanded
        if disease_name == 'Anxiety':
            if preference == 'Psychotherapy':
                rec = 'Cognitive behavioral therapy (CBT) or Acceptance and Commitment Therapy(ACT)'
            
            elif preference == 'Pharmacotherapy':
                rec = 'Lexapro-Escitalopram'
                
            else:
                rec = 'Your preference must either be Psychotherapy or Pharmcotherapy'
                
        #for different disease, different treatment is recommanded
        elif disease_name == 'Depression':
            
            if preference == 'Psychotherapy':
                rec = 'Cognitive behavioral therapy (CBT) or Dialectical Behavioral Therapy(DBT)'
            
            elif preference == 'Pharmacotherapy':
                rec = 'Celexa-Italopram'
                
            else:
                rec = 'Your preference must either be Psychotherapy or Pharmacotherapy'
        
        else:
            rec = 'Your disease name must either be Anxiety or Depression'
            
        return rec