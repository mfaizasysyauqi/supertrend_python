# Daftar Pustaka / References

> Format: APA 7th Edition  
> Semua referensi di bawah disitasi dalam kode `supertrend_python.ipynb` dan mendukung keputusan metodologis yang diambil dalam penelitian ini.

---

## A. Buku & Monograf

Burke, G. (1994). *A sharper Sharpe ratio*. *Futures*, 23(3), 56–58.  
> Digunakan sebagai justifikasi bobot Calmar Ratio (25%) dalam RAO Score. Burke berargumen bahwa drawdown adalah risiko yang paling "dirasakan" trader nyata, sehingga layak mendapat bobot signifikan dalam evaluasi strategi.

Campbell, J. Y., Lo, A. W., & MacKinlay, A. C. (1997). *The econometrics of financial markets*. Princeton University Press.  
> Digunakan sebagai referensi standar significance level α = 0.05 dalam riset keuangan empiris (hal. 17), dan sebagai acuan formulasi hipotesis statistik formal pada Cell 3.

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.  
> Digunakan sebagai referensi estimasi statistical power pada analisis bootstrap (Cell 26) dan limitasi 6.9, khususnya untuk two-sample t-test dengan jumlah trade kecil.

Efron, B., & Tibshirani, R. J. (1993). *An introduction to the bootstrap*. Chapman & Hall/CRC.  
> Disebut sebagai referensi seminal metodologi bootstrap yang digunakan pada Cell 26 (Bootstrap Simulation) untuk menghitung confidence interval metrik utama.

Elder, A. (2002). *Come into my trading room*. Wiley.  
> Digunakan sebagai justifikasi "The 2% Rule" (risk per trade = 2%) dalam RISK_PER_TRADES grid (hal. 145). Elder mendefinisikan 2% sebagai keseimbangan optimal antara pertumbuhan modal dan proteksi.

Kaufman, P. J. (2013). *Trading systems and methods* (5th ed.). Wiley.  
> Digunakan sebagai referensi threshold klasifikasi regime pasar (±3% dari MA50, hal. 147), justifikasi range parameter ATR period 3–14 (hal. 119–122), justifikasi pemilihan timeframe harian (hal. 62–63), dan justifikasi risk per trade moderat 3% untuk trend-following (hal. 342).

Lopez de Prado, M. (2018). *Advances in financial machine learning*. Wiley. [hal. 227–240, Bab 13: Backtesting through Cross-Validation]  
> Digunakan sebagai disclaimer bahwa penggunaan t-ratio Harvey et al. dalam penelitian ini merupakan aproksimasi, bukan prosedur asli Harvey, Liu & Zhu (2016). Lopez de Prado (2018) mengadaptasi Harvey et al. untuk konteks individual strategy testing.

Murphy, J. J. (1999). *Technical analysis of the financial markets*. New York Institute of Finance.  
> Digunakan sebagai referensi parameter standar industri SMA20/50 Golden/Death Cross Crossover yang digunakan sebagai benchmark ketiga (Cell 10c–10d).

Pardo, R. (2008). *The evaluation and optimization of trading strategies* (2nd ed.). Wiley.  
> Referensi utama untuk: (1) metodologi Walk-Forward Analysis (hal. 87, 201–215), (2) risiko data snooping dalam grid search, (3) justifikasi pemilihan sumber data yang konsisten untuk menghindari timestamp misalignment (hal. 87), (4) Monte Carlo reshuffling sebagai standar evaluasi edge strategi (hal. 201–215), dan (5) justifikasi desain Growing (Expanding) Window WFA (hal. 183–186).

Seban, O. (2009). *Tout sur les indicateurs techniques*. Valor Editions. ISBN: 978-2-917372-03-7. WorldCat ID: 469910993.  
> Digunakan sebagai sumber primer implementasi asli indikator SuperTrend. Merupakan referensi yang paling sering dikutip untuk standar kalkulasi SuperTrend berbasis ATR.

Thorp, E. O. (2006). The Kelly criterion in blackjack, sports betting, and the stock market. Dalam S. A. Zenios & W. T. Ziemba (Eds.), *Handbook of asset and liability management* (Vol. 1). Elsevier.  
> Digunakan sebagai justifikasi batas atas risk per trade 5% dalam RISK_PER_TRADES grid. Thorp menunjukkan bahwa praktisi menggunakan ½ Kelly atau ¼ Kelly untuk keamanan, yang menghasilkan range 5–8% untuk edge tipikal trend-following.

Van Tharp, J. (1999). *Trade your way to financial freedom*. McGraw-Hill.  
> Digunakan bersama Vince (1990) sebagai referensi Fixed Fractional Position Sizing dan justifikasi range RISK_PER_TRADES (1%–5% ekuitas per trade).

Vince, R. (1990). *Portfolio management formulas*. Wiley.  
> Referensi utama untuk Fixed Fractional Position Sizing, justifikasi range RISK_PER_TRADES, pembuktian matematis Kelly-optimal dalam jangka panjang, dan prinsip "scale with volatility" dalam position sizing ATR-based.

Wilder, J. W. (1978). *New concepts in technical trading systems*. Trend Research.  
> Digunakan sebagai referensi foundational untuk Average True Range (ATR) dan metode Wilder Smoothing (USE_TRUE_ATR=True) yang diterapkan dalam kalkulasi ATR SuperTrend. Wilder Smoothing menghasilkan nilai ATR yang lebih halus dibandingkan SMA-ATR standar.

---

## B. Artikel Jurnal & Working Papers

Bailey, D. H., & Lopez de Prado, M. (2014). The deflated Sharpe ratio: Correcting for selection bias, backtest overfitting, and non-normality. *Journal of Portfolio Management*, 40(5), 94–107. https://doi.org/10.3905/jpm.2014.40.5.094  
> Digunakan sebagai justifikasi penggunaan Mann-Whitney U test (non-parametrik) sebagai uji statistik yang lebih valid dibanding paired t-test untuk return kripto yang tidak memenuhi asumsi normalitas. Juga menjadi dasar rekomendasi t-ratio ≥ 3.0 untuk multiple comparison correction (Bagian 6.3), serta referensi karakteristik fat-tails dan skewness positif return kripto.

Brauneis, A., & Mestel, R. (2019). Cryptocurrency-portfolios in a mean-variance framework. *Finance Research Letters*, 28, 259–264.  
> Digunakan bersama Caporale et al. (2018) dan Dyhrberg (2016) sebagai preseden akademik penggunaan Rf = 0 dalam evaluasi strategi kripto berbasis Sharpe Ratio. Juga digunakan sebagai referensi batas normalisasi RAO Score (Sharpe berkisar -2 s/d +4 pada periode 2018–2023).

Camilli, G., & Hopkins, K. D. (1978). Applicability of chi-square to 2×2 contingency tables with small expected cell frequencies. *Applied Psychological Measurement*, 2(4), 461–472.  
> Disebut sebagai kritik terhadap penggunaan paired t-test pada sampel yang secara praktis bersifat independent-sample, mendukung justifikasi perlakuan uji IS vs OOS sebagai practically independent-sample test (Cell 3 / REV 6).

Caporale, G. M., Gil-Alana, L., Plastun, A., & Makarenko, I. (2018). Persistence in the cryptocurrency market. *Research in International Business and Finance*, 46, 141–148.  
> Digunakan sebagai referensi batas normalisasi RAO Score (Sharpe berkisar -2 s/d +4, Calmar -1 s/d +5 pada periode 2018–2023) dan sebagai preseden akademik penggunaan Rf = 0 untuk evaluasi strategi kripto.

D'Agostino, R. B., & Pearson, E. S. (1973). Tests for departure from normality: Empirical results for the distributions of b2 and √b1. *Biometrika*, 60(3), 613–622.  
> Digunakan sebagai referensi uji normalitas D'Agostino-Pearson yang diterapkan secara empiris pada Cell 7 (REV 10) untuk menguji distribusi return sebelum pemilihan uji statistik.

Dickey, D. A., & Fuller, W. A. (1979). Distribution of the estimators for autoregressive time series with a unit root. *Journal of the American Statistical Association*, 74(366), 427–431.  
> Digunakan sebagai referensi uji stasioneritas ADF (Augmented Dickey-Fuller) yang diterapkan secara empiris pada Cell 7 (REV 10).

Dyhrberg, A. H. (2016). Bitcoin, gold and the dollar — A GARCH volatility analysis. *Finance Research Letters*, 16, 85–92.  
> Disebut sebagai bagian dari preseden akademik penggunaan Rf = 0 secara konsisten dalam studi kripto berbasis Sharpe Ratio.

Faber, M. (2007). A quantitative approach to tactical asset allocation. *Journal of Wealth Management*, 9(4), 69–79.  
> Digunakan sebagai referensi bahwa Buy & Hold benchmark yang lebih bersih menggunakan simulasi spot (tanpa funding rate/leverage), dan sebagai referensi standar trend-following jangka menengah dalam literatur (bersama Murphy, 1999).

Harvey, C. R., Liu, Y., & Zhu, H. (2016). … and the cross-section of expected returns. *Review of Financial Studies*, 29(1), 5–68. https://doi.org/10.1093/rfs/hhv059  
> Digunakan untuk justifikasi risiko data snooping (Bagian 6.3): Harvey et al. merekomendasikan t-ratio ≥ 3.0 ketika banyak faktor/parameter diuji secara bersamaan (multiple comparison problem).

Jarque, C. M., & Bera, A. K. (1987). A test for normality of observations and regression residuals. *International Statistical Review*, 55(2), 163–172.  
> Digunakan sebagai referensi uji normalitas Jarque-Bera yang diterapkan secara empiris pada Cell 7 (REV 10) untuk menguji distribusi return.

Jobson, J. D., & Korkie, B. M. (1981). Performance hypothesis testing with the Sharpe and Treynor measures. *Journal of Finance*, 36(4), 889–908. https://doi.org/10.1111/j.1540-6261.1981.tb04891.x  
> Mendukung penggunaan Sharpe Ratio sebagai metrik risk-adjusted paling universal dalam evaluasi strategi (bobot tertinggi 35% dalam RAO Score).

Liu, Y., & Tsyvinski, A. (2021). Risks and returns of cryptocurrency. *Review of Financial Studies*, 34(6), 2689–2727.  
> Digunakan sebagai justifikasi utama penetapan RISK_FREE_ANNUAL = 0.0: investor kripto sudah menerima risiko jauh di atas risk-free asset. Juga sebagai referensi positive long-term drift BTC yang mendukung strategi long-only.

Politis, D. N., & Romano, J. P. (1994). The stationary bootstrap. *Journal of the American Statistical Association*, 89(428), 1303–1313. https://doi.org/10.1080/01621459.1994.10476870  
> Disebut sebagai alternatif yang lebih robust dibanding Monte Carlo reshuffling standar (Bagian 3 dan Bagian 6.5), khususnya untuk data time-series yang memiliki korelasi serial seperti return trend-following.

Sharpe, W. F. (1966). Mutual fund performance. *Journal of Business*, 39(1), 119–138. https://doi.org/10.1086/294846  
> Referensi seminal untuk Sharpe Ratio, yang mendapat bobot tertinggi (35%) dalam RAO Score sebagai metrik risk-adjusted paling universal.

Sortino, F. A., & van der Meer, R. (1991). Downside risk. *Journal of Portfolio Management*, 17(4), 27–31. https://doi.org/10.3905/jpm.1991.409343  
> Dasar penggunaan Sortino Ratio (bobot 20% dalam RAO Score) yang hanya menghukum downside deviation, bukan upside volatility — lebih tepat untuk strategi long-only seperti SuperTrend Long Bot ini.

Szakmary, A. C., Shen, Q., & Sharma, S. C. (2010). Trend-following trading strategies in commodity futures: A re-examination. *Journal of Banking & Finance*, 34(2), 409–426.  
> Disebut sebagai referensi pendukung temuan bahwa strategi long-only sulit mengalahkan Buy & Hold secara risk-adjusted di periode pasar yang didominasi tren naik (bull-dominant).

---

## C. Sumber Data & Referensi Teknis

Bybit Exchange. (2020–2025). *BTCUSDT linear perpetual: Historical kline & funding rate data* [Data set]. Diakses melalui Bybit V5 Public API. https://bybit-exchange.github.io/docs/v5/market/kline  
> Sumber data utama penelitian. Dipilih karena: (1) public API tanpa autentikasi, (2) ketersediaan data sejak April 2020 (peluncuran linear perpetual), (3) volume harian >$5 miliar (CoinGecko Derivatives Ranking 2024), dan (4) funding rate historis tersedia di endpoint yang sama.

Bybit Exchange. (2024). *Perpetual contract specifications*. https://www.bybit.com/en/help-center/article/Contract-Specifications-USDT-Perpetual  
> Digunakan sebagai referensi spesifikasi kontrak perpetual Bybit untuk justifikasi asumsi slippage 0.03% dan struktur biaya transaksi yang digunakan dalam backtest.

CoinGecko. (2024). *Derivatives exchange ranking*. https://www.coingecko.com/en/exchanges/derivatives  
> Digunakan sebagai referensi peringkat Bybit sebagai exchange derivatif kripto terbesar ke-2 di dunia per 2024, mendukung asumsi slippage 0.03% yang konservatif dan realistis.

---

## D. Catatan Metodologis Tambahan

### Tentang RAO Score (Risk-Adjusted Optimization Score)

RAO Score dalam penelitian ini merupakan skor komposit yang dikembangkan berdasarkan hierarki metrik dalam literatur manajemen risiko kuantitatif. Formula:

```
RAO = 0.35 × Sharpe_norm + 0.25 × Calmar_norm + 0.20 × Sortino_norm
    + 0.10 × WinRate_norm + 0.10 × ProfitFactor_norm
```

Setiap komponen dinormalisasi ke rentang [0, 1] sebelum pembobotan. Bobot dirancang agar perubahan ±5% pada bobot Sharpe dan Calmar menggeser RAO Score < 0.02 untuk parameter teratas (robustness bobot terkonfirmasi).

Batas normalisasi tiap metrik dijustifikasi berdasarkan distribusi empiris dari Caporale et al. (2018) dan Brauneis & Mestel (2019): Sharpe [-2, +4], Calmar [-1, +5], Sortino [-2, +6].

### Tentang Threshold Regime Pasar

Threshold ±3% dari MA50 untuk klasifikasi Bull/Bear/Sideways mengacu Kaufman (2013), hal. 147. Volatilitas dikategorikan relatif terhadap median historis (rolling 21 hari), mengikuti konvensi volatility regime separation dalam Pardo (2008).

### Tentang Walk-Forward Analysis

Desain WFA dalam penelitian ini menggunakan pendekatan *anchored walk-forward* (IS selalu mulai dari titik awal yang sama, diperluas setiap split), bukan *rolling window*. Pendekatan ini dipilih karena memaksimalkan data IS untuk optimasi sambil tetap menjaga integritas OOS. Lihat Pardo (2008), hal. 87–110 dan hal. 183–186.

### Tentang Penetapan Risk-Free Rate = 0%

Ditetapkan berdasarkan tiga alasan: (1) konteks aset kripto tidak memiliki instrumen bebas risiko konvensional sebagai alternatif langsung (Liu & Tsyvinski, 2021); (2) konsistensi komparasi — semua strategi dievaluasi dengan Rf yang sama; (3) preseden akademik yang konsisten dalam studi kripto (Caporale et al., 2018; Brauneis & Mestel, 2019; Dyhrberg, 2016).

### Tentang Uji Statistik Non-Parametrik

Penggunaan Mann-Whitney U test sebagai uji utama (bukan paired t-test) didasarkan pada karakteristik return kripto yang non-normal, fat-tailed, dan skewed (Bailey & Lopez de Prado, 2014), dikonfirmasi secara empiris melalui uji ADF (Dickey & Fuller, 1979), Jarque-Bera (Jarque & Bera, 1987), dan D'Agostino-Pearson (D'Agostino & Pearson, 1973).

---

*Dokumen ini merupakan bagian dari proyek SuperTrend Long Bot — Advanced Statistical Edition.*  
*Terakhir diperbarui: 2026*
