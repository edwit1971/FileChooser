##############################################################################
# In the Kivy Documentation under kivy.uix.FileChooser there is an Example
# on how to create a Popup Window that browses files and folders. It loads
# a file and saves a file.  It's in Python Code but it uses the KIVY KV
# langugae file.  Below is the same example as close as I could get it in
# pure PYTHON CODE.
#
#
# by Edmund Witkowski June 21, 2020
##############################################################################

#######################################################
#######################################################

import os

from kivy.app         import App
from kivy.core.window import Window

from kivy.uix.popup       import Popup
from kivy.uix.button      import Button
from kivy.uix.textinput   import TextInput
from kivy.uix.boxlayout   import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.relativelayout import RelativeLayout


#######################################################
#######################################################

class LoadDialog():

    #############################
    def __init__(self, **kwargs):
        super(LoadDialog, self).__init__(**kwargs)
        self.Win_To_Draw    = RelativeLayout()
        self.BoxLay1 = BoxLayout()
        self.FCL     = FileChooserListView()
        self.BoxLay2 = BoxLayout()
        self.BCancel = Button()
        self.BLoad   = Button()
        return

    #############################
    def Load_Init(self):
        #############################################
        self.Win_To_Draw.width  = int(Window.width * 0.6)
        self.Win_To_Draw.height = int(Window.height * 0.6)
        Xc = int(Window.width * 0.5)
        Yc = int(Window.height * 0.5)
        self.Win_To_Draw.x = Xc - int(self.Win_To_Draw.width * 0.5)
        self.Win_To_Draw.y = Yc - int(self.Win_To_Draw.height * 0.5)
        #############################################
        self.BoxLay1.size = self.Win_To_Draw.size
        self.BoxLay1.orientation = 'vertical'
        if(self.BoxLay1.parent == None):
            self.Win_To_Draw.add_widget(self.BoxLay1)
        #############################################
        self.FCL.size_hint_y = None
        self.FCL.height      = int(self.Win_To_Draw.height * 0.9)
        if(self.FCL.parent == None):
            self.BoxLay1.add_widget(self.FCL)
        #############################################
        self.BoxLay2.orientation = 'horizontal'
        self.BoxLay2.size_hint_y = None
        self.BoxLay2.height      = int(self.Win_To_Draw.height * 0.10)
        if(self.BoxLay2.parent == None):
            self.BoxLay1.add_widget(self.BoxLay2)
        #############################################
        self.BCancel.text = 'Cancel'
        self.BCancel.bind(on_release = Editor1.RootDialog.cancel)
        if(self.BCancel.parent == None):
            self.BoxLay2.add_widget(self.BCancel)
        #############################################
        self.BLoad.text = 'Load'
        # Using the embedded function Lambda avoids a Kivy Bug that throws an error
        self.BLoad.bind(on_release=lambda x:Editor1.RootDialog.load(self.FCL.path, self.FCL.selection))
        # Kivy Bug the following Line throws an Assertion Error about None
        #self.BLoad.bind(on_release = Editor1.RootDialog.load(self.FCL.path, self.FCL.selection))
        if(self.BLoad.parent == None):
            self.BoxLay2.add_widget(self.BLoad)
        #############################################
        return
    
#######################################################
#######################################################

class SaveDialog():

    #############################
    def __init__(self, **kwargs):
        super(SaveDialog, self).__init__(**kwargs)
        self.Win_To_Draw    = RelativeLayout()
        self.BoxLay1 = BoxLayout()
        self.FCL     = FileChooserListView()
        self.TIinput = TextInput()
        self.BoxLay2 = BoxLayout()
        self.BCancel = Button()
        self.BSave   = Button()
        return

    #############################
    def Save_Init(self):
        #############################################
        self.Win_To_Draw.width  = int(Window.width * 0.6)
        self.Win_To_Draw.height = int(Window.height * 0.6)
        Xc = int(Window.width * 0.5)
        Yc = int(Window.height * 0.5)
        self.Win_To_Draw.x = Xc - int(self.Win_To_Draw.width * 0.5)
        self.Win_To_Draw.y = Yc - int(self.Win_To_Draw.height * 0.5)
        #############################################
        self.BoxLay1.size = self.Win_To_Draw.size
        self.BoxLay1.orientation = 'vertical'
        if(self.BoxLay1.parent == None):
            self.Win_To_Draw.add_widget(self.BoxLay1)
        #############################################
        self.FCL.size_hint_y = None
        self.FCL.height      = int(self.Win_To_Draw.height * 0.8)
        self.FCL.bind(on_selection = self.Press_Save)
        if(self.FCL.parent == None):
            self.BoxLay1.add_widget(self.FCL)
        #############################################
        self.TIinput.size_hint_y = None
        self.TIinput.height      = int(self.Win_To_Draw.height * 0.1)
        self.TIinput.multiline   = False
        if(self.TIinput.parent == None):
            self.BoxLay1.add_widget(self.TIinput)
        #############################################
        self.BoxLay2.orientation = 'horizontal'
        self.BoxLay2.size_hint_y = None
        self.BoxLay2.height = int(self.Win_To_Draw.height * 0.1)
        if(self.BoxLay2.parent == None):
            self.BoxLay1.add_widget(self.BoxLay2)
        #############################################
        self.BCancel.text = 'Cancel'
        self.BCancel.bind(on_release = Editor1.RootDialog.cancel)
        if(self.BCancel.parent == None):
            self.BoxLay2.add_widget(self.BCancel)
        #############################################
        self.BSave.text = 'Save'
        # Using the embedded function Lambda avoids a Kivy Bug that throws an error
        self.BSave.bind(on_release=lambda x:Editor1.RootDialog.save(self.FCL.path, self.TIinput.text))
        # Kivy Bug the following Line throws an Assertion Error about None
        #self.BSave.bind(on_release = Editor1.RootDialog.save(self.FCL.path, self.TIinput.text))
        if(self.BSave.parent == None):
            self.BoxLay2.add_widget(self.BSave)
        #############################################
        return
    
    #############################
    def Press_Save(self):
        max = len(self.FCL.selection)
        if(max > 0):
            self.TIinput.text = self.FCL.selection[0]
        else:
            self.TIinput.text = ''
        return

#######################################################
#######################################################

class Root_FLC(FloatLayout):

    Pop1 = Popup()

    #############################
    def __init__(self, **kwargs):
        super(Root_FLC, self).__init__(**kwargs)
        self.BoxLay1 = BoxLayout()
        self.BoxLay2 = BoxLayout()
        self.BoxLay3 = BoxLayout()
        self.BLoad   = Button()
        self.BSave   = Button()
        self.TIinput = TextInput()
        return

    #############################
    def Root_Init(self):
        self.size = Window.size
        #############################################
        self.BoxLay1.size = self.size
        self.BoxLay1.orientation = 'vertical'
        if(self.BoxLay1.parent == None):
            self.add_widget(self.BoxLay1)
        #############################################
        self.BoxLay2.orientation = 'horizontal'
        self.BoxLay2.size_hint_y = None
        self.BoxLay2.height = int(self.height * 0.10)
        if(self.BoxLay2.parent == None):
            self.BoxLay1.add_widget(self.BoxLay2)
        #############################################
        self.BLoad.text = 'Load'
        self.BLoad.bind(on_release = self.show_load)
        if(self.BLoad.parent == None):
            self.BoxLay2.add_widget(self.BLoad)
        #############################################
        self.BSave.text = 'Save'
        self.BSave.bind(on_release = self.show_save)
        if(self.BSave.parent == None):
            self.BoxLay2.add_widget(self.BSave)
        #############################################
        if(self.BoxLay3.parent == None):
            self.BoxLay1.add_widget(self.BoxLay3)
        #############################################
        self.TIinput.text = ''
        if(self.TIinput.parent == None):
            self.BoxLay3.add_widget(self.TIinput)
        return
    
    def show_load(self, instance):
        Editor1.LoadDialog.Load_Init()
        ############################################
        # Content MUST point to a Parent-LESS Widget
        content = Editor1.LoadDialog.Win_To_Draw
        Root_FLC.Pop1 = Popup(title="Load file", content=content, size_hint=(0.75, 0.75))
        Root_FLC.Pop1.open()
        return

    def show_save(self, instance):
        Editor1.SaveDialog.Save_Init()
        ############################################
        # Content MUST point to a Parent-LESS Widget
        content = Editor1.SaveDialog.Win_To_Draw
        Root_FLC.Pop1 = Popup(title="Save file", content=content, size_hint=(0.75, 0.75))
        Root_FLC.Pop1.open()
        return

    def load(self, pPath='', filename=None):
        self.TIinput.text = ''
        if(filename != None):
            max = len(filename)
            if(max > 0):
                if(os.path.isdir(pPath)):
                    str = os.path.join(pPath, filename[0])
                    if(os.path.isfile(str)):
                        with open(str) as stream:
                            self.TIinput.text = stream.read()
        self.dismiss_popup()
        return

    def save(self, pPath='', filename=None):
        if(filename != None):
            if(os.path.isdir(pPath)):
                str = os.path.join(pPath, filename)
                with open(str, 'w') as stream:
                    stream.write(self.TIinput.text)
        self.dismiss_popup()
        return

    def cancel(self, instance):
        self.dismiss_popup()
        return

    def dismiss_popup(self):
        if(Root_FLC.Pop1.parent != None):
            self.Clean_Memory()
            Root_FLC.Pop1.dismiss()
        return

    def Clean_Memory(self):
        ##############################################################
        # Even with this function there is still a MEMRORY LEAK which
        # I believe to be a KIVY BUG inherent with the Popup Widget
        # so be aware there is a memory leak as the popup opens and
        # closes and opens and closes repeatedly
        ##############################################################
        Editor1.SaveDialog.BoxLay2.clear_widgets()
        Editor1.SaveDialog.BoxLay1.clear_widgets()
        Editor1.SaveDialog.Win_To_Draw.clear_widgets()
        Editor1.LoadDialog.BoxLay2.clear_widgets()
        Editor1.LoadDialog.BoxLay1.clear_widgets()
        Editor1.LoadDialog.Win_To_Draw.clear_widgets()
        Root_FLC.Pop1.clear_widgets()
        Root_FLC.Pop1.dismiss()
        Editor1.SaveDialog.Win_To_Draw.parent = None
        Editor1.LoadDialog.Win_To_Draw.parent = None
        return

#######################################################
#######################################################
# The ORIGINAL Code used...
# Factory.register('Root', cls=Root)
# Factory.register('LoadDialog', cls=LoadDialog)
# Factory.register('SaveDialog', cls=SaveDialog)
#
# But there is so little documentation explaining the
# purpose or advantages to using thie Factory.register
# Function so I just removed it because I couldn't
# figure out why it was necessary.
#
#######################################################
        
class Editor1(App):
    RootDialog = Root_FLC()
    LoadDialog = LoadDialog()
    SaveDialog = SaveDialog()
    
    def build(self):
        Editor1.RootDialog.Root_Init()
        return Editor1.RootDialog

#######################################################
#######################################################

if __name__ == '__main__':
    Editor1().run()

#######################################################
#######################################################

