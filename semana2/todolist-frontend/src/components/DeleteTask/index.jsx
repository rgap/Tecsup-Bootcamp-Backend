/* eslint-disable react/prop-types */
import { TrashIcon } from "@heroicons/react/24/solid";
import Swal from "sweetalert2";
import { destroy } from "../../services/index";
import { showError } from "../../utils";

export default function DeleteTask({ task, getTasks }) {
  const handleDeleteTask = async () => {
    const { isConfirmed } = await Swal.fire({
      title: "Esta seguro de eliminar esta tarea?",
      text: "Esta acción es irreversible",
      showCancelButton: true,
      confirmButtonText: "Eliminar",
    });

    if (!isConfirmed) return;

    const { data, ok } = await destroy(task.id, "tasks");

    if (!ok) {
      showError(data);
      return;
    }

    Swal.fire({
      text: data,
      icon: "success",
    });

    await getTasks();

    // await Swal.fire({
    //   title: "¿Seguro que la quieres eliminar?",
    //   text: "Esto no se puede revertir",
    //   icon: "warning",
    //   showCancelButton: true,
    //   confirmButtonColor: "#3085d6",
    //   cancelButtonColor: "#d33",
    //   confirmButtonText: "Si",
    // }).then(async (result) => {
    //   if (result.isConfirmed) {
    //     const { data, ok } = await destroy(task.id, "tasks");
    //     if (!ok) {
    //       showError(data);
    //       return;
    //     }
    //     await getTasks();
    //     Swal.fire("Tarea Eliminada", "", "Finalizado");
    //   }
    // });
  };

  return (
    <TrashIcon
      className="h-6 w-6 text-red-500 cursor-pointer"
      onClick={handleDeleteTask}
    />
  );
}
