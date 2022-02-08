#! /usr/bin/env python3
# https://github.com/andriykohut/docker-pyftpdlib
import argparse
import os

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.authorizers import UnixAuthorizer
from pyftpdlib.filesystems import UnixFilesystem


FTP_ROOT = '/home'


def main():
    authorizer = UnixAuthorizer(require_valid_shell=True)

    handler = FTPHandler
    handler.authorizer = authorizer # TODO - Turn on
    handler.permit_foreign_addresses = True
    
    handler.passive_ports = [3000, 3010]  # type: ignore
    handler.masquerade_address = "0.0.0.0"  # type: ignore

    server = FTPServer(("0.0.0.0", "21"), handler)
    server.serve_forever()


if __name__ == '__main__':
    main()
