from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty,StringProperty,BooleanProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.lang import Builder
from kivy.clock import Clock
import webbrowser
from rules import rule_list
from inference_engine import InferenceEngine



# Create the inference engine
inference_engine = InferenceEngine()

# Add rules to the inference engine
for rule in rule_list:
    inference_engine.add_rule(rule.antecedent, rule.consequent)

class FirstWindow(Screen):

    def click_here_button(self):
        name = self.ids.user_name.text
        print("Name :",name)
        self.ids.user_name.text = ""
        app = App.get_running_app()
        app.root.current = 'second'
        greeting_screen = app.root.get_screen('second')
        greeting_screen.set_greeting(name)

        
    pass

class SecondWindow(Screen):
    def set_greeting(self, name):
        self.ids.greeting_label.text = f"Hi {name}"

    def open_website(self, button_id):
        websites = {
            'Multimedia': 'https://fsktm.um.edu.my/bachelor-of-information-technology-multimedia',
            'Networking': 'https://fsktm.um.edu.my/bachelor-of-computer-science-computer-system-and-network',
            'AI': 'https://fsktm.um.edu.my/bachelor-of-computer-science-artificial-intelligence',
            'IS': 'https://fsktm.um.edu.my/bachelor-of-computer-science-information-systems',
            'SE': 'https://fsktm.um.edu.my/bachelor-of-computer-science-software-engineering'
            # Add more button IDs and corresponding URLs here
        }
        
        if button_id in websites:
            url = websites[button_id]
            webbrowser.open(url)

    pass


class ThirdWindow(Screen):
    pass

class Unqualified(Screen):
    pass

class Question1(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        app.root.current = next_q   
    pass


class Question2(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        app.root.current = next_q
    pass

class Question3(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        app.root.current = next_q
    pass

class Question4(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        app.root.current = next_q
    pass

class Question5(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        app.root.current = next_q
    pass

class Question6(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        app.root.current = next_q
    pass

class Question7(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        app.root.current = next_q
    pass

class Question8(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        app.root.current = next_q
    pass

class Question9(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        app.root.current = next_q
    pass

class Question10(Screen):
    def add_answer(self, answer, next_q):
        app = App.get_running_app()
        app.user_answers.append(answer)
        print("USER ANSWER :", app.user_answers)
        app.root.current = next_q
    pass

class ResultScreen(Screen):
    pass


class ProgressScreen(Screen):
    progress_value = 0
    progress_interval = 0.1

    def get_answer(self,i):
        app = App.get_running_app()
        user_ans = app.user_answers
        print('User Answer PS:', user_ans)
        # Reset user_answers to an empty list
        return user_ans

    def on_enter(self):
        Clock.schedule_interval(self.update_progress,self.progress_interval)
    
    def on_leave(self):
        Clock.unschedule(self.update_progress)
    
    def update_progress(self,dt):
        app = App.get_running_app()
        user_ans = self.get_answer(1)

        if self.progress_value >=100:
            inferred_consequents = inference_engine.infer(user_ans)
            print("Inferred Consequents : ",inferred_consequents)
            if len(inferred_consequents) > 0:
                if inferred_consequents[0] == "Software Engineer Course":
                    app.root.current = "SEScreen1"
                elif inferred_consequents[0] == "Artificial Intelligence course":
                    app.root.current = "AIScreen1"
                elif inferred_consequents[0] == "Computer System and Networking course":
                    app.root.current = "CSNScreen1"
                elif inferred_consequents[0] == "Multimedia Computing course":
                    app.root.current = "MMScreen1"
                elif inferred_consequents[0] == "Information system course":
                    app.root.current = "ISScreen1"
                else:
                    app.root.current = "UndecidedScreen"
            else:
                app.root.current = "UndecidedScreen"

            self.progress_value = 0
            self.ids.progress.value = self.progress_value
        else:
            self.progress_value += 1
            self.ids.progress.value = self.progress_value
    pass 


class SEScreen1(Screen):
    
    def SE_info_button(self):        
        self.manager.current = "SEScreen2"
    pass

class SEScreen2(Screen):
    pass

class SEScreen3(Screen):
    pass

class SEScreen4(Screen):
    def open_website(self, button_id):
        websites = {
            'GFG': 'https://www.geeksforgeeks.org/web-development/?ref=shm',
            'w3': 'https://www.w3schools.com/',
            'youtube': 'https://www.youtube.com/watch?v=fis26HvvDII'
            
            # Add more button IDs and corresponding URLs here
        }
        
        if button_id in websites:
            url = websites[button_id]
            webbrowser.open(url)

    def start_again(self):
        app = App.get_running_app()
        app.reset_user_answers()
        app.root.current = 'first'   

    pass


class AIScreen1(Screen):
    def AI_info_button(self):
        self.manager.current = "AIScreen2"
    pass

class AIScreen2(Screen):
    pass

class AIScreen3(Screen):
    pass

class AIScreen4(Screen):
    def open_website(self, button_id):
        websites = {
            'construct': 'https://www.theconstructsim.com/robotigniteacademy_learnros/ros-courses-library/',
            'coursera': 'https://www.coursera.org/learn/introduction-to-ai'
            # 'youtube': 'https://www.youtube.com/watch?v=fis26HvvDII'
            
            # Add more button IDs and corresponding URLs here
        }
        
        if button_id in websites:
            url = websites[button_id]
            webbrowser.open(url)

    def start_again(self):
        app = App.get_running_app()
        app.reset_user_answers()
        app.root.current = 'first'   

    pass


class CSNScreen1(Screen):
    def CSN_info_button(self):
        self.manager.current = "CSNScreen2"
    pass

class CSNScreen2(Screen):
    pass

class CSNScreen3(Screen):
    pass

class CSNScreen4(Screen):
    def open_website(self, button_id):
        websites = {
            'ibm': 'https://tinyurl.com/bdwj28fb',
            'GFG': 'https://www.geeksforgeeks.org/network-security/'            
            # Add more button IDs and corresponding URLs here
        }
        
        if button_id in websites:
            url = websites[button_id]
            webbrowser.open(url)

    def start_again(self):
        app = App.get_running_app()
        app.reset_user_answers()
        app.root.current = 'first'   

    pass


class MMScreen1(Screen):
    def MUL_info_button(self):
        self.manager.current = "MMScreen2"
    pass

class MMScreen2(Screen):
    pass

class MMScreen3(Screen):
    pass

class MMScreen4(Screen):
    def open_website(self, button_id):
        websites = {
            'ss': 'https://tinyurl.com/bdfwb8h6',
            'tuto': 'https://www.tutorialspoint.com/unity/index.htm'            
            # Add more button IDs and corresponding URLs here
        }
        
        if button_id in websites:
            url = websites[button_id]
            webbrowser.open(url)
    
    def start_again(self):
        app = App.get_running_app()
        app.reset_user_answers()
        app.root.current = 'first'   

    pass


class ISScreen1(Screen):
    def IS_info_button(self):
        self.manager.current = "ISScreen2"
    pass

class ISScreen2(Screen):
    pass

class ISScreen3(Screen):
    pass

class ISScreen4(Screen):
    def open_website(self, button_id):
        websites = {
            'emeritus': 'https://tinyurl.com/bdfwb8h6'
                       
            # Add more button IDs and corresponding URLs here
        }
        
        if button_id in websites:
            url = websites[button_id]
            webbrowser.open(url)

    def start_again(self):
        app = App.get_running_app()
        app.reset_user_answers()
        app.root.current = 'first'   

    pass

class Unqualified(Screen):
    def open_website(self, button_id):
        websites = {
            'qr2': 'https://study.um.edu.my/programmes.php?act=2#senarai'
        }
        
        if button_id in websites:
            url = websites[button_id]
            webbrowser.open(url) 
    pass

class UndecidedScreen(Screen):
    def open_website(self, button_id):
        websites = {
            'qr': 'https://fsktm.um.edu.my/'
        }
        
        if button_id in websites:
            url = websites[button_id]
            webbrowser.open(url)

    def start_again(self):
        app = App.get_running_app()
        app.reset_user_answers()
        app.root.current = 'first'   
    pass

class WindowManager(ScreenManager):
    pass


class CourseRecommendationApp(App):
    user_answers = []


    def build(self):
        kv = Builder.load_file("courserecommendation.kv")
        return kv

    def print_answers(self):
        print("Combined Answers:", self.user_answers)
        app = App.get_running_app()
        app.root.current = 'progress_screen'
    
    def reset_user_answers(self):
        self.user_answers = []

if __name__ == "__main__":
    CourseRecommendationApp().run()
