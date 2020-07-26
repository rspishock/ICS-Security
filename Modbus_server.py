#! /usr/bin/env python3

"""Asynchronous Modbus Server Build in Python3 using the pyModbus module."""

from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# create a datastore and populate it with test data
store = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0, [17]*100),        # Discrete inputs initializer
    co = ModbusSequentialDataBlock(0, [17]*100),        # Coils initializer
    hr = ModbusSequentialDataBlock(0, [17]*100),        # Holding register initializer
    ir = ModbusSequentialDataBlock(0, [17]*100))        # Input register initializer

context = ModbusServerContext (slaves=store, single=True)

# Populate the Modbus server information fields, these gert returned as responses to identity queries
identity = ModbusDeviceIdentification()
identity.VendorName = 'Pymodbus'
