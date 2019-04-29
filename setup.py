from setuptools import setup


setup(
    name="grpc_minder2_murmur",
    version="0.1.0",
    packages=["grpc_minder2_murmur"],
    install_requires=["grpcio", "googleapis-common-protos"],
    zip_safe=False,
)
