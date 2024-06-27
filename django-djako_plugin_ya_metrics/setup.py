from setuptools import setup, find_packages


def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="djako_plugin_ya_metrics",
    version="0.0.5",
    author="Brilev Denis",
    author_email="brilevdv@digitaleden.ru",
    description="Плагин для Djako, который предоставляет интеграцию с API Яндекс метрики и визуализирует счётчики через Chart.js",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/RedHelium?tab=repositories",
    packages=find_packages(),
    install_requires=["requests>=2.32", "Django>=5.0"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    
    keywords="Djako, Django, CMS, Web, Charts, Yandex Metrics, Admin Widgets",
    project_urls={"Documentation": "https://github.com/RedHelium?tab=repositories"},
    python_requires=">=3.10",
)
