/*grandfather(ali,abu).
parent(ali,amir).
father(amir,abu).

grandfather(ali,abu) :- parent(ali,amir),father(amir,abu). */

/*sing_a_song(ananya).   %facts
listens_to_music(rohit).		%facts

listens_to_music(ananya) :- sing_a_song(ananya).  	%rules
happy(ananya) :- sing_a_song(ananya).
happy(rohit) :- listens_to_music(rohit).
playes_guitar(rohit) :- listens_to_music(rohit).*/


/*parent(sudip,raj).
parent(sudip,lia).
male(raj).
female(lia).

sibling(X,Y) :-parent(Z,X),parent(Z,Y),male(X),female(Y). */

%facts

%courses offered
course(artificial_intelligence).
course(software_engineering).
course(computer_system_and_networking).
course(data_science).
course(information_system).
course(multimedia).

% Artificial Intelligence
requires_mathematical_understanding(artificial_intelligence).
requires_communication_skills(artificial_intelligence).
requires_analytical_logical_thinking(artificial_intelligence).
requires_attention_to_detail(artificial_intelligence).
requires_exposure_to_programming_languages(artificial_intelligence).
career_paths(artificial_intelligence, [AI_engineer, data_scientist, research_scientist]).
knowledge_of_probability_and_statistics(artificial_intelligence).
understanding_of_machine_learning_algorithms(artificial_intelligence).

% Software Engineering
differs_from_other_departments(software_engineering).
strictly_related_to_software_development(software_engineering).
higher_problem_solving_skills(software_engineering).
emphasis_on_practical_or_theory(software_engineering, practical).
required_skills(software_engineering, [programming, problem-solving, teamwork]).
emphasis_on_teamwork(software_engineering).
knowledge_of_software_quality_assurance(software_engineering).
understanding_of_software_testing_methods(software_engineering).

% Multimedia
interest_in_design_graphics(multimedia).
knowledge_of_latest_multimedia_trends(multimedia).
typical_career_paths(multimedia, [graphic_designer, multimedia_artist, web_designer]).
benefits_from_visual_style_design_intuition(multimedia).
preparation_requirements(multimedia, [art_courses, graphic_design_skills]).
knowledge_of_video_editing_and_animation(multimedia).
portfolio_building_is_important(multimedia).

% Computer System and Networking
requires_troubleshooting_problem_solving_skills(computer_system_and_networking).
exposed_to_cybersecurity_cloud_computing(computer_system_and_networking, true).
important_skills_and_qualities(computer_system_and_networking, [networking, problem-solving, attention_to_detail]).
requires_good_programming_skills(computer_system_and_networking).
scope_of_studies(computer_system_and_networking, [computer_architecture, network_protocols, operating_systems]).
exposure_to_virtualization_technologies(computer_system_and_networking).
knowledge_of_network_security(computer_system_and_networking).

% Information System
differences_from_other_departments(information_system, [skills, interest, personality]).
introduces_business_knowledge(information_system, fsktm_um).
interest_in_managing_business_using_it_solutions(information_system).
management_skills_for_future_project_manager(information_system).
requires_interest_in_business_or_entrepreneurship(information_system).
knowledge_of_database_management_systems(information_system).
understanding_of_business_analysis(information_system).

