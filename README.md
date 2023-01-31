## learning_feedback_control_systems

        
Si importa la librearia per i calcoli sui sistemi di controllo:

        import control
Siimporta la libreria per la gestione dei vettori di numeri:

        import numpy as np
        
Si importa la libreria di gestione dei grafici:

        import matplotlib.pyplot as plt

## Definiamo i vettori dei coefficienti di G1

    G1_num = np.array([1])
    G1_den = np.array([1, 3])

## Definiamo la funzione di trasferimento G1(s)

    G1 = control.tf(G1_num, G1_den)
    print('G1(s) =', G1)

## Definiamo i vettori dei coefficienti di G2(s) = G21(s) * G22(s)

    num = np.array([8])
    den = np.array([1, 2])

    G21 = control.tf(num, den)
    print('G21(s) =', G21)

    num = np.array([1])
    den = np.array([1, 1])

    G22 = control.tf(num, den)
    print('G22(s) =', G21)

## Calcoliamo G2

    G2 = G21*G22
    print('G2(s) =', G2)

## Calcolo F(s) = G1(s)*G2(s) ossia la FDT del ramo diretto:

    F = control.series(G1, G2)
     H = 4

## Calcolo la FDT del sistema ingresso-uscita retroazionato:

    W = control.feedback(F, H)
    print(W)

## Calcolo i Poli del sistema retroazionato W(s)

    p = control.poles(W)

    print('poli', p)

    control.pzmap(W)
    plt.show()

## Calcolo la risposta al gradino unitario u(t) in un intervallo di tempo coerente con le costanti di tempo del sistema

    tstart = 0
    tstop = 20
    tstep = 0.1

    t = np.arange(tstart, tstop, tstep)

    t, y = control.step_response(W, t)

## la risposta a regime si determina prendendo y[199] ossia l'ultimo valore calcolato (transitorio esaurito)

    print(y[199])

## disegno la risposta nel tempo y(t)

    plt.plot(t, y)
    plt.title("Step Response")
    plt.grid()
    plt.show()
