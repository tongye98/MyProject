from setuptools import setup, find_packages

def get_requires():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        file_content = f.read()
        lines = [line.strip() for line in file_content.strip().split("\n") if not line.startswith("#")]
        return lines 
    
def main():

    setup(
        name="MyProject",
        version="0.1.0",
        description="My project is a template.",
        long_description="My project is a template.",
        author="TongYe",
        author_email="tongye@zju.edu.cn",
        keywords=["a", "b"],
        license="MIT License",
        url="https://github.com",
        package_dir={"":"src"},
        packages=find_packages("src"),
        install_requires=get_requires(),
    )


if  __name__ == "__main__":
    main()