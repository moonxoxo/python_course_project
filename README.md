# Progetto Python Crash Course 

Un semplice programma Python che implementa una classe `Studente` per gestire informazioni personali e voti di studenti universitari.

## Funzionalità

- Presentazione dello studente
- Aggiunta di voti (validati >= 18)
- Calcolo della media
- Tracciamento ore di studio

## Struttura della classe

### Attributi
- `nome`: nome dello studente
- `cognome`: cognome dello studente
- `eta`: età dello studente
- `matricola`: numero di matricola
- `voti`: lista dei voti ottenuti

### Metodi
- `presentati()`: stampa una presentazione dello studente
- `aggiungi_voto(voto)`: aggiunge un voto se >= 18, altrimenti stampa un errore
- `calcola_media()`: calcola e stampa la media dei voti
- `studia(ore)`: stampa quante ore lo studente ha studiato
