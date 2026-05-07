#This is mcp helper file which has static methods
class MCPHelper:

    
#used to generate data for authentication 
    @staticmethod
    def generate_test_data():

        return {
            "email": "testuser@gmail.com",
            "password": "Test@123"
        }

    
#used to analyse the failure and prints
    @staticmethod
    def analyze_failure(error):

        print("MCP Failure Analysis:")

        print(f"Detected Error -> {error}")

    
#used for suggesting locators
    @staticmethod
    def suggest_locator():

        print(
            "Suggested Locator Strategy: "
            "Use ID or CSS Selector for stability"
        )