""" Part of PageObjects implementation

@author: Yevhen Bilevych

When importing internally use format: from .menu import NavigationMenu
When importing externally, use format: from webui.pages import NavigationMenu
"""
from selenium.webdriver.common.by import By
from utils.loggers import auto_steps
from webui.base import WebPage
from webui.controls import Button, Link
from ..pages import MainPage, AlertsPage, IncidentsPage, ChannelsPage, HelpPage, NotificationsPage, PeoplePage, ProfilePage, SettingsPage, ReportsPage


@auto_steps
class NavigationMenu(WebPage):

    """ Left side navigation menu page object
    It's rather pseudo-page but is a good point to start - it's available on every regular page

    """

    # WebElement references
    _search_link = Link(By.CSS_SELECTOR, 'a[uisref="modal.search"]')
    _home_page_link = Link(By.CSS_SELECTOR, 'a[uisref="home.alerts"]')
    _people_page_link = Link(By.CSS_SELECTOR, 'a[uisref="modal.people"]')
    _reports_page_link = Link(By.CSS_SELECTOR, 'a[uisref="home.reports.generate"]')
    _alerts_page_link = Link(By.CSS_SELECTOR, 'a[uisref="home.alerts"]')
    _incidents_page_link = Link(By.CSS_SELECTOR, 'a[uisref="home.incidents"]')
    _channels_page_link = Link(By.CSS_SELECTOR, 'a[uisref="home.channels"]')
    _help_page_link = Button(By.CSS_SELECTOR, 'cbp-menu-item[data-title="Help"]')
    _profile_page_link = Link(By.CSS_SELECTOR, 'a[uisref="home.profile.info"]')
    _notifications_page_link = Link(By.CSS_SELECTOR, 'a[uisref="modal.notificationCenter"]')
    _settings_page_link = Link(By.CSS_SELECTOR, "a[uisref='home.admin']")

    def open_home_page(self) -> MainPage:
        """ Open Alerts page
        :return: AlertsPage
        """
        self._home_page_link.click()
        return MainPage(self.driver)

    def open_people_page(self) -> PeoplePage:
        """ Open Alerts page
        :return: AlertsPage
        """
        self._people_page_link.click()
        return PeoplePage(self.driver)

    def open_reports_page(self) -> ReportsPage:
        """ Open Alerts page
        :return: AlertsPage
        """
        self._reports_page_link.click()
        return ReportsPage(self.driver)

    def open_alerts_page(self) -> AlertsPage:
        """ Open Alerts page
        :return: AlertsPage
        """
        self._alerts_page_link.click()
        return AlertsPage(self.driver)

    def open_incidents_page(self) -> IncidentsPage:
        """ Open Incidents page

        :return: IncidentsPage
        """
        self._incidents_page_link.click()
        return IncidentsPage(self.driver)

    def open_channels_page(self) -> ChannelsPage:
        """ Open Incidents page

        :return: IncidentsPage
        """
        self._channels_page_link.click()
        return ChannelsPage(self.driver)

    def open_help_page(self) -> HelpPage:
        """ Open Incidents page

        :return: IncidentsPage
        """
        self._help_page_link.click()
        return HelpPage(self.driver)

    def open_profile_page(self) -> ProfilePage:
        """ Open Incidents page

        :return: IncidentsPage
        """
        self._profile_page_link.click()
        return ProfilePage(self.driver)

    def open_notifications_page(self) -> NotificationsPage:
        """ Open Incidents page

        :return: IncidentsPage
        """
        self._notifications_page_link.click()
        return NotificationsPage(self.driver)

    def open_settings_page(self) -> SettingsPage:
        """ Open Incidents page

        :return: IncidentsPage
        """
        self._settings_page_link.click()
        return SettingsPage(self.driver)
