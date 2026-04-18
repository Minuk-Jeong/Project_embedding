/**
 * 스텁: 메인 OAI에 링크하지 않는다. API 시그니처·링크 검증용.
 * 실제 동작은 radio/rfsimulator/simulator.c 참고.
 */
#include "oai_sionna_bridge.h"
#include <string.h>

static char g_root[4096];

enum oai_sionna_bridge_rc oai_sionna_bridge_set_cwd(const char *project_root_abs)
{
  if (!project_root_abs)
    return OAI_SIONNA_BRIDGE_ERR_DISABLED;
  memset(g_root, 0, sizeof(g_root));
  strncpy(g_root, project_root_abs, sizeof(g_root) - 1);
  (void)g_root;
  return OAI_SIONNA_BRIDGE_ERR_STUB;
}

enum oai_sionna_bridge_rc oai_sionna_bridge_init_embed(int nr_rx, int nr_tx)
{
  (void)nr_rx;
  (void)nr_tx;
  return OAI_SIONNA_BRIDGE_ERR_STUB;
}

enum oai_sionna_bridge_rc oai_sionna_bridge_fetch_h_flat(double *out, size_t out_len,
                                                         int *out_nr_rx, int *out_nr_tx)
{
  (void)out;
  (void)out_len;
  if (out_nr_rx)
    *out_nr_rx = 0;
  if (out_nr_tx)
    *out_nr_tx = 0;
  return OAI_SIONNA_BRIDGE_ERR_STUB;
}
