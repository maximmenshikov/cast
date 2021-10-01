#!/usr/bin/env python3
# CAST project
# Author: Maxim Menshikov (maxim@menshikov.org)
import sys
import os

from cast.cast import Cast
from cast.cast_args import prepare_parser

args = prepare_parser().parse_args()
p = Cast(args.compile_db, args.template, args.output, args.workdir)
if p.validate() == False:
    sys.exit(1)

if p.translate() == False:
    sys.exit(2)
