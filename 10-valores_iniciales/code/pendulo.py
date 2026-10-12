#!/usr/bin/env python3
"""Péndulo simple: aproximación de ángulos pequeños vs. solución numérica.

    theta'' + (g / L) sen(theta) = 0,  theta(0) = theta_0,  theta'(0) = 0

Aproximación analítica (sen theta ~ theta):
    theta(t) = theta_0 cos(omega_0 t),  omega_0 = sqrt(g / L)

Período exacto del péndulo no lineal:
    T = (2 / pi) K(k) T_0,  k = sen(theta_0 / 2),  T_0 = 2 pi / omega_0
con K la integral elíptica completa de primera especie.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.special import ellipk
plt.style.use('../../utils/clases.mplstyle')

g, L = 9.81, 1.0
omega_0 = np.sqrt(g / L)
T_0 = 2 * np.pi / omega_0       # período de la aproximación lineal
t_f = 5 * T_0

def pendulo(t, z):
    theta, omega = z
    return [omega, -(g / L) * np.sin(theta)]

def theta_lineal(t, theta_0):
    return theta_0 * np.cos(omega_0 * t)

t = np.linspace(0, t_f, 1000)
angulos = [10, 45, 90]          # theta_0 en grados

fig, axs = plt.subplots(len(angulos), 1, sharex=True, figsize=(5, 5.5))
for ax, theta_0_deg in zip(axs, angulos):
    theta_0 = np.radians(theta_0_deg)
    sol = solve_ivp(pendulo, [0, t_f], [theta_0, 0.0], t_eval=t,
                    method='DOP853', rtol=1e-10, atol=1e-12)
    ax.plot(t / T_0, np.degrees(theta_lineal(t, theta_0)),
            label='Lineal (analítica)')
    ax.plot(t / T_0, np.degrees(sol.y[0]), '--',
            label='No lineal (numérica)')
    ax.set_ylabel(r"$\theta$ [$^\circ$]")
    ax.set_title(rf"$\theta_0 = {theta_0_deg}^\circ$", fontsize=16)
    error = np.max(np.abs(sol.y[0] - theta_lineal(t, theta_0))) / theta_0
    print(f"theta_0 = {theta_0_deg:3d}°: error relativo máximo = {error:.2%}")

axs[-1].set_xlabel(r"$t / T_0$")
fig.legend(*axs[0].get_legend_handles_labels(), loc='upper center', ncol=2, fontsize=13)
plt.tight_layout(rect=(0, 0, 1, 0.93))
plt.savefig("pendulo.pdf")


# Período en función de la amplitud
def cruce_cero(t, z):
    return z[0]
cruce_cero.terminal = True
cruce_cero.direction = -1

def periodo_numerico(theta_0):
    # Desde el reposo en theta_0, el péndulo tarda T/4 en llegar a theta = 0
    sol = solve_ivp(pendulo, [0, 10 * T_0], [theta_0, 0.0], events=cruce_cero,
                    method='DOP853', rtol=1e-10, atol=1e-12)
    return 4 * sol.t_events[0][0]

theta_e = np.linspace(0.1, 170, 300)            # curva exacta (grados)
T_exacto = 2 / np.pi * ellipk(np.sin(np.radians(theta_e) / 2)**2)
theta_n = np.arange(10, 171, 10)                # puntos numéricos (grados)
T_num = [periodo_numerico(np.radians(th)) / T_0 for th in theta_n]

fig, ax = plt.subplots(figsize=(5, 3.9))
ax.axhline(1, color='tab:blue', label='Lineal: $T = T_0$')
ax.plot(theta_e, T_exacto, color='tab:orange',
        label=r'Exacto: $\frac{2}{\pi} K\left(\sin\frac{\theta_0}{2}\right) T_0$')
ax.plot(theta_n, T_num, 'o', color='tab:green', label='Numérico')
for theta_0_deg in angulos:
    ax.axvline(theta_0_deg, color='gray', ls=':', lw=1)
ax.set_xlabel(r"$\theta_0$ [$^\circ$]")
ax.set_ylabel(r"$T / T_0$")
ax.legend(loc='upper left', fontsize=12)
plt.tight_layout()
plt.savefig("pendulo-periodo.pdf")

for th, Tn in zip(theta_n, T_num):
    T_ex = 2 / np.pi * ellipk(np.sin(np.radians(th) / 2)**2)
    print(f"theta_0 = {th:3d}°: T/T_0 numérico = {Tn:.8f}, exacto = {T_ex:.8f}")
