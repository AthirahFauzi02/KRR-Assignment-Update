from inference_engine import Rule

rule_list = [
        
    #Software engineer
    Rule(["No", "Logical thinker", "Yes", "Yes, I would love to!", "I love working in groups", "Hmmm, I'm not sure", "Yes, definitely", "Nah, no way", "Nah, no way", "Hmmm, I'm not sure"],["Software Engineer Course"]),

    Rule(["No", "Logical thinker", "Yes", "Yes, I would love to!", "I can adapt to any situation", "Hmmm, I'm not sure", "Yes, definitely", "Nah, no way", "Nah, no way", "Hmmm, I'm not sure"],["Software Engineer Course"]),

    Rule(["No", "Logical thinker", "Yes", "Yes, I would love to!", "I love working in groups", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way"],["Software Engineer Course"]),

    Rule(["No", "Logical thinker", "Yes", "Yes, I would love to!", "I can adapt to any situation", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way"],["Software Engineer Course"]),

    Rule(["No", "Logical thinker", "Yes", "Yes, I would love to!", "I love working in groups", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Software Engineer Course"]),

    Rule(["No", "Logical thinker", "Yes", "Yes, I would love to!", "I can adapt to any situation", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Software Engineer Course"]),
#
    Rule(["No", "Problem solver", "Yes", "Yes, I would love to!", "I love working in groups", "Hmmm, I'm not sure", "Yes, definitely", "Nah, no way", "Nah, no way", "Hmmm, I'm not sure"],["Software Engineer Course"]),

    Rule(["No", "Problem solver", "Yes", "Yes, I would love to!", "I can adapt to any situation", "Hmmm, I'm not sure", "Yes, definitely", "Nah, no way", "Nah, no way", "Hmmm, I'm not sure"],["Software Engineer Course"]),

    Rule(["No", "Problem solver", "Yes", "Yes, I would love to!", "I love working in groups", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way"],["Software Engineer Course"]),

    Rule(["No", "Problem solver", "Yes", "Yes, I would love to!", "I can adapt to any situation", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way"],["Software Engineer Course"]),

    Rule(["No", "Problem solver", "Yes", "Yes, I would love to!", "I love working in groups", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Software Engineer Course"]),

    Rule(["No", "Problem solver", "Yes", "Yes, I would love to!", "I can adapt to any situation", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Software Engineer Course"]),
#
    Rule(["No", "Detail oriented person", "Yes", "Yes, I would love to!", "I love working in groups", "Hmmm, I'm not sure", "Yes, definitely", "Nah, no way", "Nah, no way", "Hmmm, I'm not sure"],["Software Engineer Course"]),

    Rule(["No", "Detail oriented person", "Yes", "Yes, I would love to!", "I can adapt to any situation", "Hmmm, I'm not sure", "Yes, definitely", "Nah, no way", "Nah, no way", "Hmmm, I'm not sure"],["Software Engineer Course"]),

    Rule(["No", "Detail oriented person", "Yes", "Yes, I would love to!", "I love working in groups", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way"],["Software Engineer Course"]),

    Rule(["No", "Detail oriented person", "Yes", "Yes, I would love to!", "I can adapt to any situation", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way"],["Software Engineer Course"]),

    Rule(["No", "Detail oriented person", "Yes", "Yes, I would love to!", "I love working in groups", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Software Engineer Course"]),

    Rule(["No", "Detail oriented person", "Yes", "Yes, I would love to!", "I can adapt to any situation", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Software Engineer Course"]),
   
    # Artificial Intelligence    
    Rule(["Yes", "Logical thinker", "Yes", "No, I would rather focus on one language", "I love working in groups", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure"],["Artificial Intelligence course"]),

    Rule(["Yes", "Logical thinker", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure"],["Artificial Intelligence course"]),

    Rule(["Yes", "Logical thinker", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely", "Nah, no way"],["Artificial Intelligence course"]),

    Rule(["Yes", "Logical thinker", "Yes", "No, I would rather focus on one language", "I love working in groups", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely", "Nah, no way"],["Artificial Intelligence course"]),

    Rule(["Yes", "Analytical thinker", "Yes", "No, I would rather focus on one language", "I love working in groups", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure"],["Artificial Intelligence course"]),

    Rule(["Yes", "Analytical thinker", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure"],["Artificial Intelligence course"]),

    Rule(["Yes", "Analytical thinker", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely", "Nah, no way"],["Artificial Intelligence course"]),

    Rule(["Yes", "Analytical thinker", "Yes", "No, I would rather focus on one language", "I love working in groups", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely", "Nah, no way"],["Artificial Intelligence course"]),
#
    Rule(["Yes", "Detail oriented person", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure"],["Artificial Intelligence course"]),

    Rule(["Yes", "Detail oriented person", "Yes", "No, I would rather focus on one language", "I love working in groups", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely", "Nah, no way"],["Artificial Intelligence course"]),

    Rule(["Yes", "Detail oriented person", "Yes", "No, I would rather focus on one language", "I love working in groups", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure"],["Artificial Intelligence course"]),

    Rule(["Yes", "Detail oriented person", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely", "Nah, no way"],["Artificial Intelligence course"]),

    
    #CSN
    Rule(["Yes", "Problem solver", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Nah, no way", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way"],["Computer System and Networking course"]),

    Rule(["Yes", "Problem solver", "Yes", "No, I would rather focus on one language", "I prefer to work by myself most of the time", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Computer System and Networking course"]),

    Rule(["Yes", "Problem solver", "Yes", "No, I would rather focus on one language", "I prefer to work by myself most of the time", "Nah, no way", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way"],["Computer System and Networking course"]),

    Rule(["Yes", "Problem solver", "Yes", "No, I would rather focus on one language", "I love working in groups", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Computer System and Networking course"]),

    Rule(["Yes", "Detail oriented person", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Nah, no way", "Hmmm, I'm not sure", "Yes, definitely", "Nah, no way", "Nah, no way"],["Computer System and Networking course"]),

    Rule(["Yes", "Detail oriented person", "Yes", "No, I would rather focus on one language", "I prefer to work by myself most of the time", "Nah, no way", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way"],["Computer System and Networking course"]),

    Rule(["Yes", "Detail oriented person", "Yes", "No, I would rather focus on one language", "I prefer to work by myself most of the time", "Nah, no way", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Computer System and Networking course"]),

    Rule(["Yes", "Detail oriented person", "Yes", "No, I would rather focus on one language", "I love working in groups", "Hmmm, I'm not sure", "Nah, no way", "Yes, definitely", "Nah, no way", "Nah, no way"],["Computer System and Networking course"]),

    Rule(["Yes", "Detail oriented person", "Yes", "No, I would rather focus on one language", "I love working in groups", "Nah, no way", "Hmmm, I'm not sure", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Computer System and Networking course"]),

    #Multimedia
    Rule(["Yes", "Creative person", "No", "No, I would rather focus on one language", "I can adapt to any situation", "Nah, no way", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely"],["Multimedia Computing course"]),

    Rule(["Yes", "Creative person", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Nah, no way", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely"],["Multimedia Computing course"]),

    Rule(["Yes", "Creative person", "No", "No, I would rather focus on one language", "I love working in groups", "Nah, no way", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely"],["Multimedia Computing course"]),

    Rule(["Yes", "Creative person", "Yes", "No, I would rather focus on one language", "I love working in groups", "Nah, no way", "Hmmm, I'm not sure", "Nah, no way", "Nah, no way", "Yes, definitely"],["Multimedia Computing course"]),

    Rule(["Yes", "Detail oriented person", "No", "No, I would rather focus on one language", "I can adapt to any situation", "Nah, no way", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely"],["Multimedia Computing course"]),

    Rule(["Yes", "Detail oriented person", "No", "No, I would rather focus on one language", "I love working in groups", "Nah, no way", "Nah, no way", "Nah, no way", "Nah, no way", "Yes, definitely"],["Multimedia Computing course"]),

    Rule(["Yes", "Detail oriented person", "No", "No, I would rather focus on one language", "I can adapt to any situation", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely"],["Multimedia Computing course"]),

    Rule(["Yes", "Creative person", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely"],["Multimedia Computing course"]),

    Rule(["Yes", "Creative person", "No", "No, I would rather focus on one language", "I love working in groups", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely"],["Multimedia Computing course"]),

    # #Information System
    Rule(["No", "Problem solver", "Yes", "No, I would rather focus on one language", "I love working in groups", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way", "Hmmm, I'm not sure"],["Information system course"]),

    Rule(["No", "Problem solver", "Yes", "No, I would rather focus on one language", "I love working in groups", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way", "Nah, no way"],["Information system course"]),

    Rule(["No", "Problem solver", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way", "Nah, no way"],["Information system course"]),

    Rule(["No", "Problem solver", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way", "Hmmm, I'm not sure"],["Information system course"]),
    
    Rule(["No", "Problem solver", "Yes", "No, I would rather focus on one language", "I love working in groups", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely"],["Information system course"]),

    Rule(["No", "Analytical thinker", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure"],["Information system course"]),

    Rule(["No", "Analytical thinker", "Yes", "No, I would rather focus on one language", "I love working in groups", "Yes, definitely", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Hmmm, I'm not sure", "Yes, definitely"],["Information system course"]),

    Rule(["No", "Analytical thinker", "Yes", "No, I would rather focus on one language", "I can adapt to any situation", "Yes, definitely", "Nah, no way", "Nah, no way", "Nah, no way", "Nah, no way"],["Information system course"]),

]
