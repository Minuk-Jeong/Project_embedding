#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
2x2 MIMO용 FIR 임베드 진입점 (로직은 `oai_sionna_fir_embed`와 동일).

rfsimulator에서 OAI_SIONNA_FIR_MODULE=oai_sionna_fir_embed_mimo2x2 로 지정 가능.
RU/chanmod와 맞추려면 gNB·UE 모두에서 OAI_SIONNA_RX_ANT=2, OAI_SIONNA_TX_ANT=2 를 권장한다
(conf의 nb_rx/nb_tx 와 일치).
"""

from oai_sionna_fir_embed import get_fir_snapshot, init  # noqa: F401
