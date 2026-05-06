class MCPHelper:

    # ---------------- TEST DATA GENERATION ----------------

    @staticmethod
    def generate_test_data():

        return {
            "email": "testuser@gmail.com",
            "password": "Test@123"
        }

    # ---------------- FAILURE ANALYSIS ----------------

    @staticmethod
    def analyze_failure(error):

        print("MCP Failure Analysis:")

        print(f"Detected Error -> {error}")

    # ---------------- LOCATOR IMPROVEMENT ----------------

    @staticmethod
    def suggest_locator():

        print(
            "Suggested Locator Strategy: "
            "Use ID or CSS Selector for stability"
        )