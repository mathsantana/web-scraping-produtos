import undetected_chromedriver as uc

from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait


class Product:
    def __init__(
        self, name: str, price: float, market: str, image: str, link: str
    ) -> None:
        self.name = name
        self.price = price
        self.market = market


class Scraper:
    def __init__(self, market: str) -> None:
        self.market = market
        self.driver = uc.Chrome()

    def scrape() -> "list[Product]":
        raise NotImplementedError("Método scrape não implementado!")


class EconomicoScraper:
    def scrape() -> "list[Product]":
        pass


if __name__ == "__main__":
    pass
