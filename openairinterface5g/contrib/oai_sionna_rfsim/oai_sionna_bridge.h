/**
 * OAI rfsimulator — Sionna flat-H 브리지 (참조 API)
 *
 * 실제 구현은 현재 radio/rfsimulator/simulator.c 에 있음.
 * 이 헤더는 향후 리팩터/이중 경로 정리 시 계약을 고정하기 위한 스케치이다.
 */
#ifndef OAI_SIONNA_BRIDGE_H
#define OAI_SIONNA_BRIDGE_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stddef.h>

/** 브리지 초기화/갱신 결과 */
enum oai_sionna_bridge_rc {
  OAI_SIONNA_BRIDGE_OK = 0,
  OAI_SIONNA_BRIDGE_ERR_DISABLED = -1,
  OAI_SIONNA_BRIDGE_ERR_PYTHON = -2,
  OAI_SIONNA_BRIDGE_ERR_DIM = -3,
  OAI_SIONNA_BRIDGE_ERR_STUB = -99
};

/**
 * 프로젝트 루트( sionna-main 이 ./sionna-main 으로 보이는 cwd )를 기록한다.
 * 실제 구현에서는 Python sys.path 에 root/sionna-main 과 root/sionna-main/src 를 넣는다.
 */
enum oai_sionna_bridge_rc oai_sionna_bridge_set_cwd(const char *project_root_abs);

/**
 * Python 모듈 oai_channel_embed 를 로드하고 init(kwargs) 까지 수행하는 계약.
 * nr_rx, nr_tx: MIMO 안테나 수 (실제 init 인자는 구현체가 kwargs 로 맞춘다).
 */
enum oai_sionna_bridge_rc oai_sionna_bridge_init_embed(int nr_rx, int nr_tx);

/**
 * get_h_flat() 을 호출해 row-major [re,im,...] 를 out 에 채운다.
 * out_len 은 sizeof(double) * (2 * nr_rx * nr_tx) 이상이어야 한다.
 */
enum oai_sionna_bridge_rc oai_sionna_bridge_fetch_h_flat(double *out, size_t out_len,
                                                         int *out_nr_rx, int *out_nr_tx);

#ifdef __cplusplus
}
#endif

#endif /* OAI_SIONNA_BRIDGE_H */
