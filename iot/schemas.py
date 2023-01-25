from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ApplicationIds(BaseModel):
    application_id: str


class DeviceIds(BaseModel):
    device_id: str
    application_ids: ApplicationIds
    dev_eui: str
    dev_addr: str


class Identifier(BaseModel):
    device_ids: DeviceIds


class ApplicationIds1(BaseModel):
    application_id: str


class EndDeviceIds(BaseModel):
    device_id: str
    application_ids: ApplicationIds1
    dev_eui: str
    dev_addr: str


class DecodedPayload(BaseModel):
    analog_in_3: float
    analog_in_5: float
    analog_in_7: int
    digital_in_6: int
    luminosity_4: int
    relative_humidity_2: int
    temperature_1: float


class GatewayIds(BaseModel):
    gateway_id: str
    eui: str


class RxMetadatum(BaseModel):
    gateway_ids: GatewayIds
    time: str
    timestamp: int
    rssi: int
    channel_rssi: int
    snr: float
    uplink_token: str
    channel_index: int
    gps_time: str
    received_at: str


class Lora(BaseModel):
    bandwidth: int
    spreading_factor: int
    coding_rate: str


class DataRate(BaseModel):
    lora: Lora


class Settings(BaseModel):
    data_rate: DataRate
    frequency: str
    timestamp: int
    time: str


class NetworkIds(BaseModel):
    net_id: str
    tenant_id: str
    cluster_id: str
    cluster_address: str


class UplinkMessage(BaseModel):
    f_port: int
    f_cnt: int
    frm_payload: str
    decoded_payload: DecodedPayload
    rx_metadata: List[RxMetadatum]
    settings: Settings
    received_at: str
    consumed_airtime: str
    network_ids: NetworkIds


class Data(BaseModel):
    _type: str = Field(..., alias='@type')
    end_device_ids: EndDeviceIds
    correlation_ids: List[str]
    received_at: str
    uplink_message: UplinkMessage


class Context(BaseModel):
    tenant_id: str = Field(..., alias='tenant-id')


class Visibility(BaseModel):
    rights: List[str]


class Model(BaseModel):
    name: Optional[str] = None
    time: Optional[str] = None
    identifiers: Optional[List[Identifier]] = None
    data: Optional[Data] = None
    correlation_ids: Optional[List[str]] = None
    origin: Optional[str] = None
    context: Optional[Context] = None
    visibility: Optional[Visibility] = None
    unique_id: Optional[str] = None
