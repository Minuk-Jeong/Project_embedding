%% nr_rfsim_plot_bler_vs_noise_rayleigh.m
% OpenAirInterface gNB 로그(NR_MAC 주기 통계)에서 DL/UL BLER을 뽑아
% chanmod noise_power_dB 스윕 결과를 2D 플롯으로 정리합니다.
%
% 전제:
% - 4x4 2-layer Rayleigh: channelmod_rfsimu_rayleigh1_4x4.conf 의
%   noise_power_dB (enB0/ue0 동일 권장)를 스윕하고, 각 값마다 gNB를
%   일정 시간 돌린 뒤 로그를 저장합니다.
% - gNB 로그에 다음 형태가 주기적으로 찍힙니다 (openair2/.../NR_MAC_gNB/main.c):
%     UE xxxx: dlsch_rounds ... , ... BLER 0.01234 MCS ...
%     UE xxxx: ulsch_rounds ... , ... BLER 0.05678 MCS ...
%
% 사용 예:
%   T = readtable('sweep_index.csv');  % columns: noise_power_dB, gnb_log
%   plotBlerVsNoiseFromTable(T, 'meanLast', 20);
%
% 또는:
%   noiseDb = (-50:2:-30)';
%   logs    = { 'run_n50.log', 'run_n48.log', ... };  % same length as noiseDb
%   plotBlerVsNoiseFromVectors(noiseDb, logs, 'meanLast', 30);
%
% --- CSV 없이: 빌드 디렉터리에 쌓인 gNB 로그만 스캔 ---
%   plotBlerSweepFromLogGlob('/home/lab/.../cmake_targets/ran_build/build', ...
%       'GlobPattern', 'gnb_4x4_layer2_rayleigh1_*.log', 'meanLast', 30);
%
% 잡음 값을 로그에서 알아내려면 둘 중 하나를 쓰면 됩니다.
%  (A) 파일명에 np<dB>_ 삽입 (권장, tee 한 줄만 수정):
%       LOG=".../gnb_4x4_layer2_rayleigh1_np${NOISE}_$(date +%F_%H%M%S).log"
%  (B) 로그 맨 위에 마커 한 줄:
%       echo "# OAI_SWEEP noise_power_dB=${NOISE}" | tee "$LOG"
%       ... nr-softmodem ... 2>&1 | ts '...' | tee -a "$LOG"

function plotBlerSweepFromLogGlob(logDir, varargin)
  % 디렉터리에서 GlobPattern에 맞는 gNB 로그를 모두 찾아 BLER vs noise 플롯.
  % noise는 파일명 ..._np-40_2026-... 또는 로그 선두 # OAI_SWEEP noise_power_dB=-40
  p = inputParser;
  addParameter(p, 'GlobPattern', 'gnb_4x4_layer2_rayleigh1_*.log', @ischar);
  addParameter(p, 'meanLast', 25, @(x) isnumeric(x) && isscalar(x) && x > 0);
  parse(p, varargin{:});
  pat = p.Results.GlobPattern;
  K = p.Results.meanLast;
  L = dir(fullfile(logDir, pat));
  L = L(~[L.isdir]);
  if isempty(L)
    warning('No files matching %s in %s', pat, logDir);
    return;
  end
  paths = cell(numel(L), 1);
  noise = nan(numel(L), 1);
  for i = 1:numel(L)
    paths{i} = fullpathForDirEntry(logDir, L(i));
    noise(i) = extractNoisePowerDbForLog(paths{i});
  end
  valid = ~isnan(noise);
  if any(valid)
    [noiseS, ord] = sort(noise(valid));
    pathsS = paths(valid);
    pathsS = pathsS(ord);
    plotBlerVsNoiseFromVectors(noiseS, pathsS, 'meanLast', K);
    return;
  end
  % noise를 못 찾은 경우: 파일명 날짜순으로 run index 플롯
  warning(['Could not parse noise_power_dB from filenames or log headers. ', ...
           'Use np<value>_ in filename (e.g. ...rayleigh1_np-40_2026-...) ', ...
           'or first line: # OAI_SWEEP noise_power_dB=-40']);
  [~, ord] = sort({L.name});
  L = L(ord);
  paths = cell(numel(L), 1);
  for j = 1:numel(L)
    paths{j} = fullpathForDirEntry(logDir, L(j));
  end
  dlB = nan(numel(paths), 1);
  ulB = nan(numel(paths), 1);
  for j = 1:numel(paths)
    [dlB(j), ulB(j)] = summarizeLogFile(paths{j}, K);
  end
  figure('Color', 'w');
  tiledlayout(2, 1, 'TileSpacing', 'compact', 'Padding', 'compact');
  nexttile;
  plot(1:numel(dlB), dlB, '-o', 'LineWidth', 1.2);
  grid on;
  set(gca, 'XTick', 1:numel(paths), 'XTickLabel', {L.name});
  xtickangle(35);
  ylabel('DL BLER (mean last)');
  title('BLER vs log file order (noise unknown — add np<dB>_ or OAI\_SWEEP line)');
  nexttile;
  plot(1:numel(ulB), ulB, '-s', 'LineWidth', 1.2);
  grid on;
  set(gca, 'XTick', 1:numel(paths), 'XTickLabel', {L.name});
  xtickangle(35);
  ylabel('UL BLER (mean last)');
end

function np = extractNoisePowerDbForLog(logPath)
  [~, fn, ext] = fileparts(logPath);
  base = [fn, ext];
  % 파일명: ...rayleigh1_np-40_2026-04-18_120000.log
  tok = regexp(base, 'rayleigh1_np(-?\d+\.?\d*)_', 'tokens', 'once');
  if ~isempty(tok)
    np = str2double(tok{1});
    return;
  end
  % 로그 선두 24kB 안에서 마커
  fid = fopen(logPath, 'r');
  if fid < 0
    np = NaN;
    return;
  end
  chunk = fread(fid, 24000, '*char')';
  fclose(fid);
  chunk = stripAnsi(chunk);
  tok = regexp(chunk, 'OAI_SWEEP\s+noise_power_dB\s*=\s*(-?\d+\.?\d*)', 'tokens', 'once', 'ignorecase');
  if ~isempty(tok)
    np = str2double(tok{1});
    return;
  end
  tok = regexp(chunk, 'noise_power_dB\s*=\s*(-?\d+\.?\d*)', 'tokens', 'once', 'ignorecase');
  if ~isempty(tok)
    np = str2double(tok{1});
    return;
  end
  np = NaN;
end

function plotBlerVsNoiseFromTable(T, varargin)
  % T: table with variables 'noise_power_dB' and 'gnb_log' (full paths)
  p = inputParser;
  addParameter(p, 'meanLast', 25, @(x) isnumeric(x) && isscalar(x) && x > 0);
  parse(p, varargin{:});
  n = T.noise_power_dB(:);
  L = T.gnb_log(:);
  if ~iscell(L)
    L = cellstr(L);
  end
  plotBlerVsNoiseFromVectors(n, L, 'meanLast', p.Results.meanLast);
end

function plotBlerVsNoiseFromVectors(noise_power_dB, logPaths, varargin)
  p = inputParser;
  addParameter(p, 'meanLast', 25, @(x) isnumeric(x) && isscalar(x) && x > 0);
  parse(p, varargin{:});
  K = p.Results.meanLast;
  n = noise_power_dB(:);
  assert(numel(n) == numel(logPaths));

  dlB = nan(size(n));
  ulB = nan(size(n));
  for i = 1:numel(n)
    [dl, ul] = summarizeLogFile(logPaths{i}, K);
    dlB(i) = dl;
    ulB(i) = ul;
  end

  figure('Color', 'w');
  tiledlayout(2, 1, 'TileSpacing', 'compact', 'Padding', 'compact');
  nexttile;
  plot(n, dlB, '-o', 'LineWidth', 1.2);
  grid on;
  xlabel('noise\_power\_dB (OAI chanmod)');
  ylabel('DL BLER (gNB log, mean last samples)');
  title('4x4 Rayleigh + AWGN-like noise: DL BLER vs noise\_power\_dB');

  nexttile;
  plot(n, ulB, '-s', 'LineWidth', 1.2);
  grid on;
  xlabel('noise\_power\_dB (OAI chanmod)');
  ylabel('UL BLER (gNB log, mean last samples)');
  title('UL BLER vs noise\_power\_dB');
end

function [dlMean, ulMean] = summarizeLogFile(logPath, meanLast)
  txt = fileread(logPath);
  txt = stripAnsi(txt);
  lines = strsplit(txt, sprintf('\n'));
  dl = [];
  ul = [];
  for k = 1:numel(lines)
    ln = lines{k};
    if contains(ln, 'dlsch_rounds') && contains(ln, 'BLER')
      v = extractBlerAfterToken(ln, 'BLER');
      if ~isempty(v)
        dl(end+1) = v; %#ok<AGROW>
      end
    end
    if contains(ln, 'ulsch_rounds') && contains(ln, 'BLER')
      v = extractBlerAfterToken(ln, 'BLER');
      if ~isempty(v)
        ul(end+1) = v; %#ok<AGROW>
      end
    end
  end
  dlMean = tailMean(dl, meanLast);
  ulMean = tailMean(ul, meanLast);
end

function v = extractBlerAfterToken(line, token)
  % First BLER on DL line; UL line also has single BLER before MCS on UL branch
  idx = strfind(line, token);
  if isempty(idx)
    v = [];
    return;
  end
  % take first occurrence (DL line has one BLER; UL line has one BLER)
  rest = line(idx(1)+numel(token):end);
  tok = regexp(rest, '^\s*([0-9]*\.?[0-9]+([eE][+-]?[0-9]+)?)', 'tokens', 'once');
  if isempty(tok)
    v = [];
  else
    v = str2double(tok{1});
  end
end

function m = tailMean(v, K)
  v = v(:);
  if isempty(v)
    m = NaN;
    return;
  end
  n = min(K, numel(v));
  m = mean(v(end-n+1:end));
end

function p = fullpathForDirEntry(logDir, d)
  if isfield(d, 'folder') && ~isempty(d.folder)
    p = fullfile(d.folder, d.name);
  else
    p = fullfile(logDir, d.name);
  end
end

function s = stripAnsi(s)
  s = regexprep(s, sprintf('\x1B\\[[0-9;]*[a-zA-Z]'), '');
end

%% ---- Example driver (uncomment and edit paths) ----
% plotBlerSweepFromLogGlob('/home/lab/바탕화면/Project_embedding/openairinterface5g/cmake_targets/ran_build/build');
%
% T = table( ...
%   (-46:2:-34)', ...
%   { ...
%     '/full/path/gnb_rayleigh_np-46.log', ...
%     '/full/path/gnb_rayleigh_np-44.log', ...
%     ... % one row per noise point
%   }, ...
%   'VariableNames', {'noise_power_dB','gnb_log'});
% plotBlerVsNoiseFromTable(T, 'meanLast', 30);
