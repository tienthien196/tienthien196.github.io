import sys, time, hashlib
from java.io import PrintWriter

from burp import IBurpExtender
from burp import IHttpRequestResponse
from burp import IHttpService
from burp import ISessionHandlingAction

token = '6a70067c4af280aae184de6ab026ffa9'
secret = 'DP{y6E<9NIf3t1x@'

PARAM_URL = 0
PARAM_BODY = 1
PARAM_COOKIE = 2
PARAM_XML = 3
PARAM_XML_ATTR = 4
PARAM_MULTIPART_ATTR = 5
PARAM_JSON = 6

class BurpExtender(IBurpExtender, ISessionHandlingAction):

    def getActionName(self):
        # return extension name
        return 'My Custom Headers'

    def registerExtenderCallbacks(self, callbacks):
        # set extension name
        callbacks.setExtensionName("My Custom Headers")

        # register for scanner callbacks
        callbacks.registerSessionHandlingAction(self)

        # make errors more readable ad required for debugger burp-exceptions
        sys.stdout = callbacks.getStdout()

        # use PrintWriter for all output
        self.stdout = PrintWriter(callbacks.getStdout(), True)
        self.stderr = PrintWriter(callbacks.getStdout(), True)

        # write a message to output stream
        self.stdout.println("My Custom Headers")

        # keep reference to the callbacks
        self.callbacks = callbacks

        # obtain extension to the helper object
        self.helpers = callbacks.getHelpers()

    def performAction(self, baseRequestResponse, macroItems):
        # analyse request to be modified
        request_details = self.helpers.analyzeRequest(baseRequestResponse)
        # get headers
        headers = request_details.getHeaders()
        # get full request
        message = baseRequestResponse.getRequest()
        # get request body
        requestStr = self.helpers.bytesToString(message)
        requestParsed = self.helpers.analyzeRequest(message)
        body_offset = requestParsed.getBodyOffset()
        message_body = requestStr[body_offset:]
        get_final_headers = request_details.getHeaders()
        # get paramaters
        parameters = request_details.getParameters()[0:]
        # get method
        request_method = request_details.getMethod()
        if request_method == 'GET':
            return

        for header in headers:
            if header.strip().startswith("Token:"):
                get_final_headers.remove(header)
            if header.strip().startswith("Time:"):
                get_final_headers.remove(header)
            if header.strip().startswith("Sign:"):
                get_final_headers.remove(header)

        currentTime = str(time.time()).split('.')[0]+'100'

        is_json = message_body[0] == '{' or message_body[0] == '[';
        if is_json:
            md5params = hashlib.md5(message_body.encode('utf-8')).hexdigest()
            params = ''
        else:
            md5params = 'd41d8cd98f00b204e9800998ecf8427e'
            params = list(message_body.split('&'))
            params.sort()
            params = "&".join(params)

        Sign = hashlib.md5((token + secret + currentTime + params + md5params).encode('utf-8')).hexdigest()

        get_final_headers.add('Token: '+ token)
        get_final_headers.add('Time: '+ currentTime)
        get_final_headers.add('Sign: '+ Sign)
        httpRequest = self.helpers.buildHttpMessage(get_final_headers, message_body)
        baseRequestResponse.setRequest(httpRequest)
