# --- Importing Libraries ---
import json
import types
import os
import importlib.resources as pkg_resources
from NumScript.source import json as json_pkg  # package folder for JSON files

# --- NumScript Virtual Machine ---
class NumScriptVirtualMachine:
    
    # --- Setup of "Global variables" ---
    def __init__(self):
        
        # --- Defining Global variables ---
        self.math = ["++", "--", "**", "//", ">>", "<<", "==", "&&", "||", "~~"]  # List of math symbols
        self.nsascii = {
            "00": "a", "01": "b", "02": "c", "03": "d", "04": "e", "05": "f", "06": "g",
            "07": "h", "08": "i", "09": "j", "10": "k", "11": "l", "12": "m", "13": "n",
            "14": "o", "15": "p", "16": "q", "17": "r", "18": "s", "19": "t", "20": "u",
            "21": "v", "22": "w", "23": "x", "24": "y", "25": "z", "26": "A", "27": "B",
            "28": "C", "29": "D", "30": "E", "31": "F", "32": "G", "33": "H", "34": "I",
            "35": "J", "36": "K", "37": "L", "38": "M", "39": "N", "40": "O", "41": "P",
            "42": "Q", "43": "R", "44": "S", "45": "T", "46": "U", "47": "V", "48": "W",
            "49": "X", "50": "Y", "51": "Z", "52": "0", "53": "1", "54": "2", "55": "3",
            "56": "4", "57": "5", "58": "6", "59": "7", "60": "8", "61": "9", "62": "!",
            "63": "\"", "64": "#", "65": "$", "66": "%", "67": "&", "68": "'", "69": "(",
            "70": ")", "71": "*", "72": "+", "73": ",", "74": "-", "75": ".", "76": "/",
            "77": ":", "78": ";", "79": "<", "80": "=", "81": ">", "82": "?", "83": "@",
            "84": "[", "85": "\\", "86": "]", "87": "^", "88": "_", "89": "`", "90": "{",
            "91": "|", "92": "}", "93": "~", "94": "€", "95": "£", "96": "¥", "97": "¢",
            "98": "§", "99": " "
        }
        self.reversedNSAscii = {v: k for k, v in self.nsascii.items()}

        # --- Interpreter state variables ---
        self.indexChange = 1
        self.lindex = 0
        self.higherLindex = 0
        self.tokenizedCode = []
        self.higherTokenizedCode = []
        self.depth = 0
        self.maxDepth = 0
        self.variables = {}
        self.stacks = {}
        self.definitions = {}
        self.currentDefinition = ""
        self.loopCallback = False

        # --- Load JSON module paths ---
        with pkg_resources.open_text(json_pkg, "modulePaths.json") as f:
            modulesToImport = json.load(f)

        for modulePath, functionName in modulesToImport.items():
            module = __import__(f"NumScript.source.{modulePath}", fromlist=[functionName])
            func = getattr(module, functionName)
            setattr(self, functionName, types.MethodType(func, self))

        # --- Load interpreter settings ---
        with pkg_resources.open_text(json_pkg, "settings.json") as f:
            settings = json.load(f)

        self.states = settings["states"]
        self.shellInSymbol = settings["symbols"]["shellIn"]
        self.shellOutSymbol = settings["symbols"]["shellOut"]
        self.input_symbol = settings["symbols"]["input"]

        # File paths
        self.codePath = settings["paths"]["codePath"]
        self.definitionsPath = settings["paths"]["definitionsPath"]
        self.filesPath = settings["paths"]["filesPath"]
        self.stacksPath = settings["paths"]["stacksPath"]
        self.variablesPath = settings["paths"]["variablesPath"]

        # --- Init code if enabled ---
        if settings.get("init", False):
            with pkg_resources.open_text(json_pkg, "1318.ns", encoding="utf-8") as f:
                importedCode = [line.rstrip("\n") for line in f]
                for line in importedCode:
                    line = self.tokenizer(line.replace(" ", ""))
                    self.tokenizedCode.append(line)
                self.run()

        # --- Ensure user-writable data folders exist ---
        base_path = os.path.expanduser("~/.numscript")
        for folder in ["code", "definitions", "files", "stacks", "variables"]:
            path = os.path.join(base_path, folder)
            os.makedirs(path, exist_ok=True)
