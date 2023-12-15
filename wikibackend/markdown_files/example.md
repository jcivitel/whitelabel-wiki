```php
<?php
// Verbindung zur MySQL-Datenbank herstellen
$servername = "Dein_Servername";
$username = "Dein_Benutzername";
$password = "Dein_Passwort";
$dbname = "Dein_Datenbankname";

$conn = new mysqli($servername, $username, $password, $dbname);

// Überprüfen, ob die Verbindung erfolgreich ist
if ($conn->connect_error) {
    die("Verbindung fehlgeschlagen: " . $conn->connect_error);
}

// SQL-Befehl zum Erstellen eines Backups
$backupFile = 'backup.sql';
$query = "mysqldump --user={$username} --password={$password} --host={$servername} {$dbname} > $backupFile";
exec($query);

// Verbindung schließen
$conn->close();

echo "Backup erfolgreich erstellt!";
?>
```

### Erklärung:

1. **Verbindung zur MySQL-Datenbank herstellen:**
   - `$servername`: Der Name des Servers, auf dem die Datenbank läuft.
   - `$username`: Der Benutzername für die Datenbankverbindung.
   - `$password`: Das Passwort für die Datenbankverbindung.
   - `$dbname`: Der Name der Datenbank, für die das Backup erstellt werden soll.

2. **Verbindung überprüfen:**
   - Es wird überprüft, ob die Verbindung zur Datenbank erfolgreich hergestellt wurde. Falls nicht, wird das Skript mit einer Fehlermeldung beendet.

3. **SQL-Befehl zum Erstellen eines Backups:**
   - Ein Befehl wird zusammengesetzt, um das `mysqldump`-Tool aufzurufen, das ein Backup der MySQL-Datenbank erstellt.
   - Der Befehl wird mit dem `exec`-Befehl ausgeführt.

4. **Verbindung schließen:**
   - Die Verbindung zur Datenbank wird geschlossen, nachdem das Backup erstellt wurde.

5. **Ausgabe:**
   - Eine Erfolgsmeldung wird ausgegeben, wenn das Backup erfolgreich erstellt wurde.
