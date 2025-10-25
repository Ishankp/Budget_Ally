from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class IndividualWatchlistCode(str, Enum):
    au_con = "AU_CON"
    ca_con = "CA_CON"
    eu_con = "EU_CON"
    iz_cia = "IZ_CIA"
    iz_ipl = "IZ_IPL"
    iz_pep = "IZ_PEP"
    iz_unc = "IZ_UNC"
    uk_hmc = "UK_HMC"
    us_dpl = "US_DPL"
    us_dtc = "US_DTC"
    us_fbi = "US_FBI"
    us_fse = "US_FSE"
    us_isn = "US_ISN"
    us_mbc = "US_MBC"
    us_plc = "US_PLC"
    us_sdn = "US_SDN"
    us_ssi = "US_SSI"
    sg_sof = "SG_SOF"
    tr_twl = "TR_TWL"
    tr_dfd = "TR_DFD"
    tr_for = "TR_FOR"
    tr_wmd = "TR_WMD"
