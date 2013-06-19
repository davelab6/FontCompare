#! /usr/bin/python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import time
from fc.FontCompare import *
from fc.GlyphConsistency import *

# Import the interface class
from fc import main_ui
 
class MainApp(QMainWindow, main_ui.Ui_MainWindow):

    Testfilepath = ""
    Standardfilepath = ""
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)#?????????????
        # This is because Python does not automatically
        # call the parent's constructor.
        self.setupUi(self)
        self.connectActions()
 
    def connectActions(self):
        self.BeginTestButton.clicked.connect(self.BeginTest)
        self.loadTestpushButton.clicked.connect(self.OpenTestFile)
        self.loadStandardpushButton.clicked.connect(self.OpenStandardFile)
        self.ClearMessageBoxButton.clicked.connect(self.ClearMessage)
        self.SaveMessageBoxButton.clicked.connect(self.SaveMessage)

    def BeginTest(self):
        if self.ParametersCheckBox.isChecked():
            self.TestFromStandards(1)
        else:
            self.TestFromFont()

    def OpenTestFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Test File')
        if fontforge.open(filename):
            QMessageBox.about(self, "Success", "The file was loaded successfully!")
            self.Testfilepath = filename
            return
        else:
            QMessageBox.about(self, "Error", "The file could not be loaded!\n Please try again")

    def OpenStandardFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Standard File')
        if fontforge.open(filename):
            QMessageBox.about(self, "Success", "The file was loaded successfully!")
            self.Standardfilepath = filename
            return
        else:
            QMessageBox.about(self, "Error", "The file could not be loaded!\n Please try again")

    def ClearMessage(self):
        self.MessageBox.setText("")

    def SaveMessage(self):
        content = self.MessageBox.toPlainText()
        savefilename = QFileDialog.getSaveFileName(self, 'Save File')
        myfile=open(savefilename,'w')
        myfile.write(content)
        myfile.close()

    def TestFromStandards(self,choice):
        self.PrintMessage("under construction")

    def PrintGlyphrelatedScore(self,scores):
        start = time.clock()
        for score in scores:
            self.PrintMessage(str(score))
        total=len(scores)
        final=0
        for gtuple in scores:
            final+=gtuple[1]
        if final:
            final = (final/float(total))/10
        else:
            final = 0
            self.PrintMessage("The test font has no glyphs for Selected Script Unicode characters")

        elapsed = (time.clock() - start)    
        self.PrintMessage("The total score was "+str(final))
        self.PrintMessage("The execution time was "+str(elapsed))
        return final

    def TestFromFont(self):
        if not self.Testfilepath or not self.Standardfilepath:
            QMessageBox.about(self, "Warning!","Please load standard or test file")
        fontA = fontforge.open(self.Testfilepath)
        fontB = fontforge.open(self.Standardfilepath)
        fc=FontCompare()
        gc=GlyphConsistency()
        #consistency test
        #numerals
        score = gc.glyph_basicset_consistency(fontA, (0x960,0x96f))
        self.PrintMessage("Numeral Consistency Score is "+str(score))
        self.NumeralScoreBar.setValue(round(score))
        #consonants
        score = gc.glyph_basicset_consistency(fontA, (0x915,0x939))
        self.PrintMessage("Consonant Consistency Score is "+str(score))
        self.ConsonantScoreBar.setValue(round(score))
        #marks
        score = gc.glyph_basicset_consistency(fontA, (0x958,0x95f))
        self.PrintMessage("Mark Consistency Score is "+str(score))
        self.MarkScoreBar.setValue(round(score))
        #vowels
        score = gc.glyph_basicset_consistency(fontA, (0x904,0x914))
        self.PrintMessage("Vowel Consistency Score is "+str(score))
        self.VowelScoreBar.setValue(round(score))
        #rounding 
        score = gc.glyph_round_consistency(fontA, self.GetScript())
        self.PrintMessage("Rounding Consistency Score is "+str(score))
        self.RoundingScoreBar.setValue(round(score))
        #normal test
        scores = fc.font_facecompare(fontA,fontB,self.GetScript(),600,12,1,"normal")
        score =  self.PrintGlyphrelatedScore(scores)
        self.NormalScoreBar.setValue(round(score))
        #bold test
        scores = fc.font_facecompare(fontA,fontB,self.GetScript(),600,12,1,"bold")
        score = self.PrintGlyphrelatedScore(scores)
        self.BoldScoreBar.setValue(round(score))
        #italic test
        scores = fc.font_facecompare(fontA,fontB,self.GetScript(),600,12,1,"italic")
        score = self.PrintGlyphrelatedScore(scores)
        self.ItalicScoreBar.setValue(round(score))

    def GetScript(self):
        return (0x901,0x970)#self.LanguageBox.currentIndex()

    def GetFontFilePaths(self):
        print "under construction"

    def PrintMessage(self,message):
        self.MessageBox.append(message)


    def main(self):
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.main()
    app.exec_()
