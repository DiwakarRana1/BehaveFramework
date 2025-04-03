class TabHandler:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_new_tab(self):
        """Switch to the newly opened tab."""
        window_handles = self.driver.window_handles  # Get all open tabs
        if len(window_handles) > 1:
            self.driver.switch_to.window(window_handles[-1])  # Switch to the last opened tab
        else:
            raise Exception("New tab was not opened.")

    def close_current_tab_and_switch_back(self):
        """Close the current tab and switch back to the original window."""
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            self.driver.close()  # Close the current tab
            self.driver.switch_to.window(window_handles[0])  # Switch back to the first tab
        else:
            raise Exception("No new tab to close.")
