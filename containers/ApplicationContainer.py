from dependency_injector import containers, providers
from clients import DMTelegramClient
from services import LoguruLoggingService, ScraperService
from scrapers import TelegramScraper

__author__ = 'Sergey K. aka unix3dgforce'
__copyright__ = 'Copyright (c) 2024 Sergey K.'


class ApplicationContainer(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    logging = providers.Singleton(
        LoguruLoggingService,
        configuration=configuration.log
    )

    scrapers = providers.Dict({
        "telegram": providers.Factory(
            TelegramScraper,
            client=providers.Factory(
                DMTelegramClient,
                configuration=configuration.scrapers.telegram.client,
                logger=logging
            ),
            configuration=configuration.scrapers.telegram,
            logger=logging
        )
    })

    scraper_service = providers.Factory(
        ScraperService,
        scrapers=scrapers,
        logger=logging
    )
